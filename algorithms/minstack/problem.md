Min Stack
---

[Leetcode problem link](https://oj.leetcode.com/problemset/algorithms/)

This is not a problem that leads to heap sort, nope. This is a problem where it's a little more interesting. We can do four operations on the stack.

- Push(x): push x on to the stack
- Pop(): pop the top of the stack
- Top(): return the top of the stack
- getMin(): return the min element in the stack

All operations are required to be finished in constant time (O(1)).

I used python for this problem since python is the easiest to work with in terms of lists, dynamic growth etc. 

There are a few problems I face when writing this assignment. OJCode don't generate a new instance of your class when switch between test cases, so you have to write your constructors, otherwise there will be errors. 