import asyncio
import re
import secrets


from webdriver import get_web_driver


class StdOutIterableSingleton:

    def __init__(self, proc):
        self.stdout_stream = proc.stdout
        self.current_output = []
        self.done = False
        self.lock = asyncio.Lock()

    def __aiter__(self):
        return StdOutIterator(self)

    async def _read_char(self):
        value = (await self.stdout_stream.read(1)).decode('unicode_escape')
        if value == '':
            raise StopAsyncIteration
        else:
            self.current_output.append(value)
        return value


class StdOutIterator:

    def __init__(self, std_out_iterable):
        self.std_out_iterable = std_out_iterable
        self.count = 0

    async def __anext__(self):
        async with self.std_out_iterable.lock:
            if self.count < len(self.std_out_iterable.current_output):
                value = self.std_out_iterable.current_output[self.count]
                self.count += 1
                return value
            if self.std_out_iterable.done:
                raise StopAsyncIteration
            else:
                value = await self.std_out_iterable._read_char()
                self.count += 1
                return value


async def print_output(output):
    async for char in output:
        print(char, end="")


async def line_by_line(output):
    current = ""
    async for c in output:
        if c == "\n":
            ret = current
            current = ""
            yield ret
        else:
            current += c



async def main():

    # create process
    proc = await asyncio.subprocess.create_subprocess_exec(
        'python', 'currate.py',
        stdin=asyncio.subprocess.PIPE,
        stdout=asyncio.subprocess.PIPE,
    )

    output = StdOutIterableSingleton(proc)

    printing_task = asyncio.create_task(print_output(output))

    async for line in line_by_line(output):
        match = re.search('Go to the following URL: (https://.*)', line)
        if match is not None:
            url = match.group(1)
            driver = get_web_driver()
            output_url = await get_output_url(url, driver)
            print(output_url)
            driver.close()
            proc.stdin.write((output_url + "\n").encode())
            await proc.stdin.drain()


    await printing_task

    print("finished!!")


if __name__ == '__main__':
    asyncio.run(main())
