#Excel Sheet Column Number

[leetcode problem link](https://oj.leetcode.com/problems/excel-sheet-column-number/)

This problem is turn a string of `AABB` into a number like what we have in excel.

I used python to solve this problem (since manipulating string is so easy in python ..). I used currentDigit * (26^i), where i is the current digit we at in order to calculate the number.

It's like, your number is base 26, not base 10