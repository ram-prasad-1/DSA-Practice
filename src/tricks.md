# DS Algo Tricks
## Dump
Use hash map to find something quick

## DP
### 1. Two Sum
```javascript
b = sum - a
```

### 121. Best Time to Buy and Sell Stock
Just keep track of min. value found so far.
<https://tenderleo.gitbooks.io/leetcode-solutions-/content/GoogleEasy/121.html>

### 53. Maximum Subarray
```javascript
dp[i] = max(dp[i-1] + nums[i], nums[i])
```
See: [53. Maximum Subarray](https://medium.com/tech-life-fun/leet-code-53-maximum-subarray-detailed-explained-python3-solution-d91c7affc02a)


## Mix
### Middle Value Overflow
```text
mid = (left + right)/2   ==>   mid = left + (right - left)/2
```
See: <https://www.code-recipe.com/post/overflow-binary-search>
