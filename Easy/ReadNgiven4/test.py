
# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
	def read(self, buf, n):
		"""
		:type buf: Destination buffer (List[str])
		:type n: Maximum number of characters to read (int)
		:rtype: The number of characters read (int)
		"""
		idx = 0
	  	while n > 0:
			buffer = ['']*4
	  		l = read4(buffer)
	  		if not l:
		  		return 0

		  	for i in range(min(l, n)):
				buf[idx] = buf4[i]
			  	idx += 1
			  	n -= 1
		return idx



