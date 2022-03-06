from enum import Enum

import numpy as np

class Note(Enum):
    C = 0
    G = 1
    D = 2
    A = 3
    E = 4
    B = 5
    H = 6
    K = 7
    P = 8
    T = 9
    V = 10
    F = 11


def circ(note):

    val = np.pi*(float(note.value) / 6.0)
    return np.array([np.cos(val), np.sin(val)])


# c_lin = np.array([[1.0], [0.0], [0.0]]) @ circ(Note.C).reshape((1, -1))
#
# e_c_com = (circ(Note.E) @ circ(Note.C)) * circ(Note.C)
# e_c_orth_com = circ(Note.E) - e_c_com
#
# e_ket = - (c_lin @ circ(Note.E)).reshape((-1, 1)) + np.array([[0.0], [1.0], [0.0]])
# e_bra = e_c_orth_com.reshape((1, -1)) / np.linalg.norm(e_c_orth_com) ** 2
#
# c_e_lin = c_lin + e_ket @ e_bra



start = np.array([1.0, 1.0, 1.0]) / 3.0

c_lin = (np.array([[1.0], [0.0], [0.0]]) - start.reshape((-1, 1))) @ circ(Note.C).reshape((1, -1))
e_c_com = (circ(Note.E) @ circ(Note.C)) * circ(Note.C)
e_c_orth_com = circ(Note.E) - e_c_com
e_ket = -(c_lin @ circ(Note.E)).reshape((-1, 1)) + np.array([[0.0], [1.0], [0.0]]) - start.reshape((-1, 1))
e_bra = e_c_orth_com.reshape((1, -1)) / np.linalg.norm(e_c_orth_com) ** 2
c_e_lin = c_lin + e_ket @ e_bra

def temperature(value, t):
    return value
    # value = t * value
    # return np.exp(value) / np.sum(np.exp(value))

def note_to_color(note: Note):
    return temperature(c_e_lin @ circ(note) + start, 1.0)

def note_to_rgb(note: Note):
    return np.round(note_to_color(note) * 255)

for note in Note:
    print(f"{note.name} => {note_to_rgb(note)}")



def circle_of_fifths(note):
    value =  7.0 * note
    while value >= 12.0:
        value -= 12.0
    return value

def mapping(v):
    return 2 ** (v/12.0)

def rev_map(a):
    value = np.log2(a) * 12.0
    while value >= 12.0:
        value -= 12.0
    return value

print(rev_map(3.0))
print(circle_of_fifths(rev_map(3.0)))
print(rev_map(5.0))
print(circle_of_fifths(rev_map(5.0)))
print(circle_of_fifths(4.0))
print(circle_of_fifths(2.0))