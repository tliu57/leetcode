class Solution(object):
	def hasCycle(self, head):
		slow = head
		fast = head
		while True:
			if not fast or not fast.next:
				return False
			slow = slow.next
			fast = fast.next.next
			if slow == fast:
				return True 
