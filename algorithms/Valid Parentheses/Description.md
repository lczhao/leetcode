#Valid Parenthese

[leetcode problem discription](https://oj.leetcode.com/problems/valid-parentheses/)

The idea is to validate parentheses in the input

This algorithm was written in python and does a linear scan over the input, and count the number of parentheses of each type. At the end, check if every count is zero.

This algorithm also check if we validate the rule by closing parentheses by keeping the last opened parens in a list, and validate it when we hit a closing one `} ] )`.

This will prevent `{ [ } ]`

This algorithm finishes in `O(n)`