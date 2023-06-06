# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# def opSeq(l, opType="Reverse"):
#     if opType == "ListToInt": # List to Integer
        
#         return 
#     elif opType == "IntToList": # Integer to List
#         l = str(l)
#         return [int(l[x]) for x in range(-1, -len(l)-1, -1)]

class Solution:
    def toInteger(self, li):
        temp = li
        n = ""
        while True:
            n += str(temp.val)
            temp = temp.next
            if temp == None:
                break
            if temp.next == None:
                n += str(temp.val)
                break
        return int(n[::-1])

    def toList(self, num: int):
        first = temp = None
        for x in str(num)[::-1]:
            if temp == None:
                first = temp = ListNode(x)
                continue
            temp.next = ListNode(x)
            temp = temp.next
        return first

    def addTwoNumbers(self, l1, l2):
        p1 = self.toInteger(l1)
        p2 = self.toInteger(l2)
        print(p1, p2, p1 + p2)
        return self.toList(self.toInteger(l1) + self.toInteger(l2))

a = Solution()
li1 = [9,9,9,9,9,9,9]
li2 = [9,9,9,9]
f1 = None
f2 = None
temp = []
for x in li1:
    # print(x)
    if f1 == None:
        f1 = ListNode(x)
        temp = f1
    else:
        temp.next = ListNode(x)
        temp = temp.next
for x in li2:
    if f2 == None:
        f2 = ListNode(x)
        temp = f2
    else:
        temp.next = ListNode(x)
        temp = temp.next


print(a.addTwoNumbers(a.toList(0), a.toList(0)).val)