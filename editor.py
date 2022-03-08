from define_tbuf import *
from utility_tbuf import *


class Editor:
    def __init__(self, row, col):
        self.buf = TextBuffer()
        self.row = row
        self.col = col

# A valid editor data structure is:
# - non-NULL
# - has a valid text buffer
# - has recorded row and col fields
# - that match tbuf_row() and tbuf_col()
def is_editor(editor: Editor) -> bool:
    if not editor:
        return False

    buf = TextBuffer()
    row, col = buf.row, buf.col

    return is_tbuf(buf) and tbuf_row(buf) == row and tbuf_col(buf) == col


