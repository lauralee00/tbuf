from define_tbuf import *
from utility_tbuf import *
from editor import *


#TODO: print_text()

def tbuf_content(B):
    if tbuf_is_empty(B): return ""

    start, end, cursor = B.start, B.end, B.cursor
    res = []
    while start != end:
        start = start.next
        if start == cursor:
            res += "|"
        if start.data:
            res += start.data
    return "".join(res)


def test():
    new = editor_new()
    B = new.buf
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
            print(new.buf.cursor.data, end="")
            editor_forward(new)
        print("\nGood Job 2")
    except:
        print("\nBad 2")

def main() -> None:
    if input("Press y to create a text editor. ").lower() == 'y':
        E = editor_new()
        B = E.buf
    else:
        print("Oh well.")
        return

    help_toggle = True
    content_toggle = True

    while True:
        if content_toggle:
            print("Enter quit to exit.")
            print("Here are the updated contents. If you don't want contents to be displayed after every command, enter no-update.")
            print("Instead, you can see the texts by entering display. Enter update for continuous display.")
            print(tbuf_content(B))

        if help_toggle:
            print("Enter left, right, down, up to navigate through the text.")
            print("Enter backspace to delete message behind the cursor, displayed as |.")
            print("All single character inputs will be considered as inserts behind the cursor, displayed as |.")
            print("Entering empty messages will be considered a line break.")
            print("To create new text, enter new.")
            print("If you no longer want to see these messages, enter no-help.")
            print("Enter help to have them displayed after every user command.")

        msg = input().lower()
        if msg == "quit":
            break
        elif msg == "update":
            content_toggle = True
        elif msg == "help":
            help_toggle = True
        elif msg == "new":
            E = editor_new()
            B = E.buf
        elif msg == "no-update":
            content_toggle = False
        elif msg == "no-help":
            help_toggle = False
        elif not content_toggle and msg == "display":
            print(tbuf_content(B))
        elif msg == "left":
            editor_backward(B)
        elif msg == "right":
            editor_forward(B)
        # elif msg == "down":
        # elif msg == "up":
        elif len(msg) == 1: # input
            editor_insert(B, msg)
        elif msg == "": # no input enter will count as new line
            editor_insert(B, "\n")
        elif msg == "backspace":
            editor_delete(B)
        else:
            for c in msg:
                editor_insert(B, c)

















if __name__ == "__main__":
    main()
