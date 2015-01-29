#Largest Number

[leetcode problem link](https://oj.leetcode.com/submissions/detail/19482390/)

In this problem, we were asked to find the largest number that a list of numbers can possibly form.

This is a very interesting question, since one of the most intuitive algorithm is to find all the combination and compute the largest. (which could be done in O(n!), since n! is the all possible permutation of a list with length n)

However, if we think more like a computer, we can sort this list of numbers (descending), then just output `A[1] .. A[n]`.

Of course, we would have to use a custom sorting, but it is much better then O(n!), in fact, it's `O(n log n)`. Now, that's the power of computer science :)

---

This solution was written in C++, because we want speed! In fact, this algorithm finishes in 22ms, which super impressed me!