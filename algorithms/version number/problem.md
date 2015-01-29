#Version Number

[leetcode problem link](https://oj.leetcode.com/problems/compare-version-numbers/)

This problem is a fairly easy problem if you know some library functions in C++ or python

All I did was splitting the version number using ".", and compare each digit. 

I append "0" at the shorter array since we might have the case `1.0 == 1` or `1.0.3 == 1`, by appending zeros, this problem simply reduced to `1.0 == 1.0` and `1.0.3 == 1.0.0`. Which at this case, all we have to do is to loop through the digit.

This problem was written in python, and achieved one of the fastest runtime in leetcode submission. (We are using library functions!)