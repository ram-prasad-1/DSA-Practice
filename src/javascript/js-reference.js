// JS references

```
Trick: In JS everything is stored in heap only including primitives.
and each value has an address(=reference) attached to it.
So in variables we just save these addresses only.

The references in JavaScript only point at contained values
and NOT at other variables, or references. (=== pass by reference-value)

https://www.zhenghao.io/posts/javascript-variables#why-javascript-can-not-do-pass-by-reference
```
let man = {name: "Joe Doe"};
let human = [man];
man =  null;
console.log(human); // [{...}]
