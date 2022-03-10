from define_tbuf import *
from utility_tbuf import *
from typing import *


class Editor:
    def __init__(self, row: Optional[int], col: Optional[int], buf: Optional[TextBuffer]):
        self.buf = buf
        self.row = row
        self.col = col

# implementation:

# A valid editor data structure is:
# - non-NULL
# - has a valid text buffer
# - has recorded row and col fields
# - that match tbuf_row() and tbuf_col()
def is_editor(editor: Editor) -> bool:
    if not editor:
        return False

    buf = editor.buf
    row, col = buf.row, buf.col

    return is_tbuf(buf) and tbuf_row(buf) == row and tbuf_col(buf) == col


# interface functions:

# Create a new and empty editor
def editor_new() -> Editor:
    # ENSURES: is_editor(\result)
    new = Editor(row=1, col=0, buf=tbuf_new())
    return new

# Move the cursor forward, to the right
def editor_forward(E: Editor) -> None:
    if not is_editor(E): raise ValueError
    buf = E.buf
    if buf.cursor != tbuf_at_right(buf):
        tbuf_forward(buf)
        if buf.cursor.prev.data == '\n': # new line
            E.row += 1
            E.col = 0
        else: # cur line
            E.col += 1

# Move the cursor backward, to the left
def editor_backward(E: Editor) -> None:
    if not is_editor(E): raise ValueError
    buf = E.buf
    if not tbuf_at_left(buf):
        tbuf_backward(buf)
        if buf.cursor.data == "\n":
            E.row -= 1
            E.col = tbuf_col(buf)
        else:
            E.col -= 1

# Insert c to the cursor’s left
def editor_insert(E: Editor, c: str) -> None:
    if not is_editor(E): raise ValueError
    tbuf_insert(E, c)

# Remove the node to the cursor’s left
def editor_delete(E: Editor) -> None:
    buf = E
    if is_tbuf(buf) and not tbuf_is_empty(buf) and not buf.cursor.prev == buf.start:
        tbuf_delete(buf)


# TODO: implement editor_up() and editor_down()
# # moves cursor one line above
# # preserves original column unless new line has fewer columns
# #   in which case cursor is placed at the rightmost column
# def editor_up(E: Editor) -> None:
#     r, c = tbuf_row(B), tbuf_col(B)
#     if r == 1: #first line
#         return
#     while E.buf.cursor.data != "\n":
#         editor_forward(E)
#
#     newC = tbuf_col(B)
#     for i in range(c-newC):
#         editor_forward(E)
#         if E.buf.cursor.data == "\n":
#             break
#
#
# # moves cursor one line below
# # preserves original column unless new line has fewer columns
# #   in which case cursor is placed at the rightmost column
# def editor_down(E: Editor) -> None:
#     r, c = tbuf_row(E), tbuf_col(E)
#     if r == E.row:
#         return
#     while E.buf.cursor.data != "\n":
#         editor_backward(E)
#
#     for i in range(c):
def editor_up(E: Editor) -> None:              # Moves the cursor up #
    if not is_editor(E): raise ValueError
    crow = E.row # current row
    ccol = E.col # current col
    if crow != 1: # top row, can't go up
        nrow = crow-1
    while E.row != nrow:
        editor_backward(E)
    # rightmost col of prev row
    ncol = min(ccol, tbuf_col(E.buf));
    # ccol if ccol is less than total col of prev row
    # or total col if not enough row
    while E.col != ncol:
        editor_backward(E)
    assert(is_editor(E))

def editor_down(E: Editor) -> None:            # Moves the cursor down
    if not is_editor(E): raise ValueError
    crow = E.row # current row
    ccol = E.col # current col
    nrow = crow+1
    while (E.row != nrow and  not tbuf_at_right(E.buf)):
        editor_forward(E)
        if (E.row != nrow and tbuf_at_right(E.buf)): # last row, can't go down
            # former cond takes care of edge case when
            # moving down from last col of 2nd to last row
            # to last col of last row
            while (E.col != ccol):
                editor_backward(E) # return to original col of original row
        elif (E.row == nrow):
            assert(E.col == 0); # leftmost col
            while (not tbuf_at_right(E.buf) and E.row == nrow && E.col != ccol):
                editor_forward(E) # go to original col of new row
            # if (tbuf_at_right(E.buf)): # last row, not enough col
            #     pass
            if (E.row != nrow): #not enough col, moved to next line
              assert(E.row > nrow)
              editor_backward(E) # go one back
              assert(E.row == nrow) # last col of prev row (not enough cols)
            else:
                assert(E.col == ccol and E.row == nrow)
    else:
        raise ValueError



