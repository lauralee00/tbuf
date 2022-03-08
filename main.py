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

        print("\nBad 1")
    except:
        print("\nGood Job 1")

    try:
        for i in range(7):
            print(E.buf.cursor.data, end="")
            editor_forward(E)
        print("\nGood Job 2")
    except:
        print("\nBad 2")

if __name__ == "__main__":
    main()
