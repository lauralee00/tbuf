import sys

input = lambda: sys.stdin.readline().strip()
read = lambda: map(int, input().split())

from define_tbuf import *
from utility_tbuf import *
from editor import *

def main():
    E = editor_new()
    B = E.buf
    for c in "hello":
        tbuf_insert(B, c)

    try:
        for i in range(7):
            print(B.cursor.data, end="")
            tbuf_backward(B)

        print("Bad 1")
    except:
        print("Good Job 1")

    try:
        for i in range(7):
            print(E.buf.cursor.data, end="")
            editor_backward(E)
        print("Good Job 2")
    except:
        print("Bad 2")

