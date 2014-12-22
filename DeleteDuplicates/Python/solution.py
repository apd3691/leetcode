import sys
sys.path.insert(0, '/home/casey/Desktop/CodingProblems/leetcode/Testing/Python')#linux
sys.path.insert(0, '/Users/CaseyMcGuire/Desktop/leetcode/Testing/Python')#mac
from ListNode import *
import unittest

def deleteDuplicates(head):
    if head is None:
        return None
        
    cur_node = head
    next_node = head.next

    while True:
        if next_node is None:
            cur_node.next = None
            break
        elif cur_node.val != next_node.val:
            cur_node.next = next_node
            cur_node = next_node
        next_node = next_node.next
    return head



#TESTS
class TestDeleteDuplicates(unittest.TestCase):
    
    def setUp(self):
        self.duplicate_lists = [
            None

        ]

        self.deleted_lists = [
            None
        ]


    def test_lists(self):
        

    if __name__ == '__main__':
        unittest.main()