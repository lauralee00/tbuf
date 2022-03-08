import typing
from define_tbuf import *




# the cursor is as far left as possible
def tbuf_at_left(B: TextBuffer) -> bool:
    # REQUIRES: is_tbuf(B)
    start, cursor = B.start, B.cursor
    return True if cursor == start.next else False

# the cursor is as far right as possible
def tbuf_at_right(B: TextBuffer) -> bool:
    # REQUIRES: is_tbuf(B)
    end, cursor = B.end, B.cursor
    return True if cursor == end else False

# interface functions for manipulating doubly-linked lists with cursors:

# Create a new and empty text buffer
def tbuf_new() -> TextBuffer:
    # REQUIRES: None
    # ENSURES: is_tbuf(\result) && tbuf_empty(\result)
    new = TextBuffer()
    mid = DllNode(None)
    new.start.next = new.end.prev = mid
    mid.prev, mid.next = new.start, new.end
    new.cursor = new.end
    return new

# Move the cursor forward, to the right
def tbuf_forward(B: TextBuffer) -> None:
    # REQUIRES: is_tbuf(B) and B.cursor != B.end
    # ENSURES: is_tbuf(B) (esp checking for cursor_in_range(B))

    if not is_tbuf(B): raise ValueError

    if B.cursor != B.end:
        B.cursor = B.cursor.next
    else: raise ValueError


# Move the cursor backward, to the left
def tbuf_backward(B: TextBuffer) -> None:
    # REQUIRES: is_tbuf(B) and B.cursor != B.start.next
    # ENSURES: is_tbuf(B) (esp checking for cursor_in_range(B))
    if not is_tbuf(B): raise ValueError

    if B.cursor != B.start.next:
        B.cursor = B.cursor.prev
    else: raise ValueError

# Insert c to the cursor’s left
def tbuf_insert(B: TextBuffer, c: str) -> None:
    # REQUIRES: is_tbuf(B)
    # ENSURES: is_tbuf(B)
    if not is_tbuf(B): raise ValueError

    cursor = B.cursor
    new = DllNode(c)
    cleft = cursor.prev

    cleft.next = cursor.prev = new
    new.prev, new.next = cleft, cursor


# Remove the node to the cursor’s left (should return the deleted char)
def tbuf_delete(B: TextBuffer) -> str:
    # REQUIRES: is_tbuf(B) && not tbuf_is_empty(B) && tbuf.cursor.prev != tbuf.start
    # ENSURES: is_tbuf(B)
    if not is_tbuf(B) or tbuf_is_empty(B): raise ValueError

    start, end, cursor = B.start, B.end, B.cursor
    if cursor.prev == start:
        raise ValueError  # can't delete start

    nleft, nright = cursor.prev.prev, cursor
    nleft.next, cursor.prev = cursor, nleft

def tbuf_row(B: TextBuffer) -> int:  # Return the row of the cursor
    # REQUIRES: is_tbuf(B)
    # ENSURES: is_tbuf(B) && (\result) >= 1
    if not is_tbuf(B): raise ValueError

    start, end, cursor = B.start, B.end, B.cursor
    rowCount = 1
    while cursor != start.next:
        cursor = cursor.prev
        # if (cursor.data == "\n") it's the line before
        if cursor.data == "\n":
            rowCount += 1
    return rowCount

def tbuf_col(B: TextBuffer) -> int:	 # Return the column of the cursor
    # REQUIRES: is_tbuf(B)
    # ENSURES: is_tbuf(B) && (\result) >= 0
    if not is_tbuf(B): raise ValueError


    start, end, cursor = B.start, B.end, B.cursor
    colCount = 0
    while cursor != start.next or cursor.prev.data != "\n":
        # former case addresses cursor in first row
        colCount += 1
        cursor = cursor.prev
        # breaks loop when cursor == start.next or when cursor.data is "\n"
    return colCount
