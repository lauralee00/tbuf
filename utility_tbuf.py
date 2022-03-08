import typing
from define_tbuf import *

# the cursor is as far left as possible
def tbuf_at_left(B: TbufHeader) -> bool:
    return False

# the cursor is as far right as possible
def tbuf_at_right(B: TbufHeader) -> bool:
    return False

# interface functions for manipulating doubly-linked lists with cursors:

# Create a new and empty text buffer
def tbuf_new() -> TbufHeader:
    return TbufHeader()

# Move the cursor forward, to the right
def tbuf_forward(B: TbufHeader) -> None:
    return

# Move the cursor backward, to the left
def tbuf_backward(B: TbufHeader) -> None:
    return

# Insert c to the cursor’s left
def tbuf_insert(B: TbufHeader, c: str) -> None:
    return

# Remove the node to the cursor’s left (should return the deleted char)
def tbuf_delete(B: TbufHeader) -> str:
    return "a"
