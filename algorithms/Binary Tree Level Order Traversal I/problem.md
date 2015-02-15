Binary Tree Level Order Traversal
----

[leetcode problem link](https://oj.leetcode.com/problems/binary-tree-level-order-traversal/)

This is a binary tree problem. Which is a fairly common data type.

There are three ways to travel in a binary tree:

- Inorder
- Preorder
- Postorder

However, this question is none of the above, it's a level order traversal.
 This means we print out level 1 first, then level 2 ... so on.
 
 I used a queue in order to solve the problem, my queue works like this..
 
		q = [root] ...
		c = q.pop()
		q.push(c.left, c.right) => q = [left, right]
		c = q.pop();
		q.push(c.left, c.right) => q = [right, left.left, left.right]
		
This way, I am able to establish level order traversal just by using a queue