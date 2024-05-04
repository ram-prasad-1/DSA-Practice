Service Team

Some DS&A questions from service side : 

Write a function to deep clone object
Implement curry function which should work like this 
function multiply(a, b, c) {  return a * b * c;}
let curried = curry(multiply);
console.log(curried(2)(3)(4)); // 24
console.log(curried(2, 3)(4));  // 24
console.log(curried(2, 3, 4));  // 24
console.log(curried(5)(6, 7)); // 210

Find target element index in sorted array. If element is not present find index at which it would have been present 
const nums = [1,3,4,5,7,8]
const target = 2
result : 1
Function to convert number to base 2 or base 10 : if num = 14 and base 2 - o/p : 1110
convert binary max-heap to binary  min-heap : [9,4,7,1,-2,6,5] => [-2,1,5,9,4,6,7]

Accounting Team
Find the length of the longest substring that has all unique characters
Given an array of size n and a number 0 < k <= n, divide the array into k partitions, compute sum of the maximum value of each partition, maximize this sum over all possible k-partitions of the array
Calculate the sum of depths of all the nodes in a binary tree

 

Parts Team
Create Card deck and shuffler (will clear basic implementation of arrays and oops concept)

Implementation of debounce in javascript

Implement sum with n number of arguments and n number of invocation -  sum(1,2..n)(5,6…n)…(n)()

React -> implement useState using javascript (can ignore the re-render trigger thing)

Provided 2 dimensional array , print them in sprial order - logic thinking , just approach is fine 

Sometimes (when I nest (parenthesis) too much (like this (and this))) - they get confusing
Write a function that, given a sentence like the one above, along with the position of an opening parenthesis, finds the corresponding closing parenthesis.

Example: if the example string above is input with the number 10 (position of the first parenthesis), the output should be 71 (position of the last parenthesis).

 

DRP Team
1>Overlaping range merge in Javascript (Array)
Input:- [[1,3],[2,5],[4,6]]
Output:- [[1,6]]]
Input:- [[1,3],[2,5],[4,6], [7,8]]
Output:- [[1,6],[7,8]]
Input:- [ [7,8],[1,3],[2,5],[4,6]]
Output:- [[1,6],[7,8]]
Input:- [[1,5],[2,3]]
Output:- [[1,5]]]

2>length of longest sequence without duplicate in javascript (String) 
console.log(lengthOfLongestSubstring("abcabcbb")); // 3
console.log(lengthOfLongestSubstring("bbbbb")); // 1
console.log(lengthOfLongestSubstring("abcdef")); // 6
console.log(lengthOfLongestSubstring("")); // 0

3>Custom javascript function for deep comparison of object (Object)
var obj = {here: {is: "an"}, object: [2]};
console.log(deepEqual(obj, obj));
// → true 
console.log(deepEqual(obj, {here: 1, object: 2}));
// → false 
console.log(deepEqual(obj, {here: {is: "an"}, object: [2]}));
// → true 

Retail
1. Given an array representing prices of the stock on different days, find the maximum profit that can be earned by performing maximum of one transaction.
       Example: {100, 80, 120, 130, 70, 60, 100, 125} Profit: 65
2. On continuation to above one, Given an array of stock prices, find the maximum profit that can be earned by performing multiple non-overlapping transactions (buy and sell).
       Example: {100, 80, 120, 130, 70, 60, 100, 125} Profit: 115
3. Write a function to find spiral traversal of a matrix
const input = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9, 10, 11, 12],
  [13, 14, 15, 16],
];
const output = [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10];
4. Find the next minimum element for all the elements of an array. (can be done using stack)
5. Given a pair of text and pattern, find if the pair forms an anagram. (Sliding Window Pattern)
Eg: tekion - text & bio - pattern -> YES, tekion - text & eke - pattern -> NO
