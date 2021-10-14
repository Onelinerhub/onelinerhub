# How to reverse the words in a phrase

``` C#
("This tests that").Split(' ').Aggregate((a,b) => b + " " + a);
```
- .Split(' ') - splits a string by using a space ' ' separator
- .Aggregate - gather every one other element a, in an element list to a target element b
- (a,b) => b + " " + a - arrow function taking input arguments (a,b) used to concatenate b gathered character argument in the list in reverse with " " space separator to the targeted character argument a