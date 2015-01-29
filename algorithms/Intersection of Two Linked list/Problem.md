#Linked List intersection

[leetcode problem link](https://oj.leetcode.com/problems/intersection-of-two-linked-lists/)

This solution was written in C++ (it's easier to manipulate pointers ...).

This problem is interesting because it restricts our run time to O(n) and space to O(1). (Aside, O(n^2) would be easy, lol)

The idea of this solution is to calculate the length of both linked list first, and then get rid of the extra content that's for sure will not be a part of the intersection.

Then, do a linear search over the leftovers in O(n).

		A1 -> | A2 -> A3\
			  |			 -> C4 -> C5...
			  | B1 -> B2/
			 
			<= I don't care what's before this..

