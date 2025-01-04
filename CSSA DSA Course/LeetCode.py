#2
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution(object):
#     def deleteDuplicates(self, head):
#         """
#         :type head: ListNode
#         :rtype: ListNode
#         """
#         if not head:
#             return head
        
#         current = head
#         while current and current.next:
#             if current.val == current.next.val:
#                 current.next = current.next.next
#             else:
#                 current = current.next
        
#         return head



#3
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# class Solution(object):
#     def getIntersectionNode(self, headA, headB):
#         """
#         :type headA: ListNode
#         :type headB: ListNode
#         :rtype: ListNode
#         """
#         if not headA or not headB:
#             return None

#         currentA, currentB = headA, headB
#         while currentA != currentB:
#             currentA = currentA.next if currentA else headB
#             currentB = currentB.next if currentB else headA
#         return currentA
  
    
#4
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution(object):
#     def swapPairs(self, head):
#         """
#         :type head: ListNode
#         :rtype: ListNode
#         """
#         current = head
#         ab = []
#         while current and current.next:
#             ab.append(current.next.val)
#             ab.append(current.val)
#             current = current.next.next
        
#         if current:
#             ab.append(current.val)
        
#         dummy = ListNode(0)
#         tail = dummy
#         for val in ab:
#             tail.next = ListNode(val)
#             tail = tail.next
#         return dummy.next


#5
# class Solution(object):
#     def reverseBetween(self, head, left, right):
#         """
#         :type head: ListNode
#         :type left: int
#         :type right: int
#         :rtype: ListNode
#         """
#         dummy = ListNode(0)
#         dummy.next = head
#         prev = dummy
        
#         for _ in range(left - 1):
#             prev = prev.next
        
#         reverse_start = prev.next
#         curr = reverse_start.next
#         for _ in range(right - left):
#             reverse_start.next = curr.next
#             curr.next = prev.next
#             prev.next = curr
#             curr = reverse_start.next       
#         return dummy.next





#stacks
#1
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution:
#     def isPalindrome(self, head: ListNode) -> bool:
#         vals = []
#         current = head
#         while current:
#             vals.append(current.val)
#             current = current.next
        
#         return vals == vals[::-1]

#2
# class Solution:
#     def isValid(self, s: str) -> bool:
#         stack = []
#         matching_parentheses = {')': '(', '}': '{', ']': '['}
        
#         for char in s:
#             if char in matching_parentheses.values():
#                 stack.append(char)
#             elif char in matching_parentheses.keys():
#                 if stack and stack[-1] == matching_parentheses[char]:
#                     stack.pop()
#                 else:
#                     return False

#         return len(stack) == 0

#3
# from collections import deque

# class MyStack:

#     def __init__(self):
#         self.queue1 = deque()
#         self.queue2 = deque()

#     def push(self, x: int) -> None:
#         self.queue1.append(x)

#     def pop(self) -> int:
#         while len(self.queue1) > 1:
#             self.queue2.append(self.queue1.popleft())
        
#         popped_element = self.queue1.popleft()
        
#         self.queue1, self.queue2 = self.queue2, self.queue1
        
#         return popped_element

#     def top(self) -> int:
#         while len(self.queue1) > 1:
#             self.queue2.append(self.queue1.popleft())
        
#         top_element = self.queue1.popleft()
        
#         self.queue2.append(top_element)
        
#         self.queue1, self.queue2 = self.queue2, self.queue1
        
#         return top_element

#     def empty(self) -> bool:
#         return len(self.queue1) == 0


#4
# class Solution:
#     def calPoints(self, operations: List[str]) -> int:
#         record = []
        
#         for op in operations:
#             if op == '+':
#                 record.append(record[-1] + record[-2])
#             elif op == 'D':
#                 record.append(2 * record[-1])
#             elif op == 'C':
#                 record.pop()
#             else:
#                 record.append(int(op))
        
#         return sum(record)


#5
# class Solution:
#     def lengthLongestPath(self, input: str) -> int:
#         path_lengths = {0: 0}
#         max_length = 0

#         for line in input.splitlines():
#             level = line.count('\t')
#             name = line.lstrip('\t')
            
#             if '.' in name:  
#                 max_length = max(max_length, path_lengths[level] + len(name))
#             else:  
#                 path_lengths[level + 1] = path_lengths[level] + len(name) + 1  
        
#         return max_length





#queues
#2
# class Solution:
#     def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
#         time = 0
        
#         for i in range(len(tickets)):
#             while tickets[k] > 0:
#                 for j in range(len(tickets)):
#                     if tickets[j] > 0:
#                         tickets[j] -= 1
#                         time += 1
#                     if j == k and tickets[k] == 0:
#                         return time
#         return time

#3
# from collections import deque

# class Solution:
#     def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
#         deck.sort()
        
#         index_queue = deque()
        
#         for i in range(len(deck)):
#             index_queue.append(i)
        
#         result = [0] * len(deck)
        
#         for card in deck:
#             result[index_queue.popleft()] = card
#             if index_queue:
#                 index_queue.append(index_queue.popleft())
        
#         return result


#4
# class Solution:
#     def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
#         MOD = 10**9 + 7
#         dp = [0] * (n + 1)
#         dp[1] = 1  
        
#         total_people_sharing = 0  
        
#         for day in range(2, n + 1):
#             if day - delay >= 1:
#                 total_people_sharing = (total_people_sharing + dp[day - delay]) % MOD
            
#             if day - forget >= 1:
#                 total_people_sharing = (total_people_sharing - dp[day - forget]) % MOD
            
#             dp[day] = total_people_sharing
        
#         total_people = 0
#         for day in range(n - forget + 1, n + 1):
#             total_people = (total_people + dp[day]) % MOD
        
#         return total_people

#5
# class DataStream:
#     def __init__(self, value: int, k: int):
#         self.value = value  
#         self.k = k          
#         self.count = 0      

#     def consec(self, num: int) -> bool:
#         if num == self.value:
#             self.count += 1  
#         else:
#             self.count = 0    
        
#         return self.count >= self.k



