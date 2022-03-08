import typing

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class DllNode:
    def __init__(self, data: str):
        self.data = data
        self.next = None
        self.prev = None


class TextBuffer:
    def __init__(self):
        self.start = DllNode()
        self.cursor = self.start
        self.end = DllNode()

def is_dll_segment(a: DllNode, b: DllNode) -> bool:
    if a == b: return False # edge case (size 1)
    head, tail = a, b

    while head and head != tail:
        head = head.next

    if head != tail: return False

    head = a

    while tail and tail != head:
        tail = tail.prev

    return True if tail == head else False

#requires is_dll_segment(a, b)
def is_circular_dll(a: DllNode, b: DllNode) -> bool:
    try:
        slow = a
        fast = a.next
        while slow is not fast:
            slow = slow.next
            fast = fast.next.next
        return True

        slow = b
        fast = b.prev
        while slow is not fast:
            slow = slow.prev
            fast = fast.prev.prev
        return True
    except:
        return False

# checks if cursor in (head, tail] --------> (assumes is_segment and no cycle)
def cursor_in_range(tbuf: TextBuffer) -> bool:
    head, tail, cursor = tbuf.start, tbuf.end, tbuf.cursor
    while head != tail:
        head = head.next
        if head == cursor: return True
    return False

# a valid text buffer is a non-Null tbuf* with the following properties:
# - the "next" links proceed from the "start" node to the "end" node
# - with the cursor node included in the segment from "start" (exclusive) to "end" (inclusive)
# - "prev" mirrors the "next" links
def is_tbuf(tbuf: TextBuffer) -> bool:
    head, tail, cursor = tbuf.start, tbuf.end, tbuf.cursor
    if not is_dll_segment(head, tail): return False
    if is_circular_dll(head, tail): return False
    if not cursor_in_range(tbuf): return False

    return True

def tbuf_is_empty(tbuf: TextBuffer) -> bool:
    if not is_tbuf(tbuf): raise ValueError

    head, tail, cursor = tbuf.start, tbuf.end, tbuf.cursor
    if (head.next == tail and tail.prev == head) and (cursor == tail):
        return True
    return False











