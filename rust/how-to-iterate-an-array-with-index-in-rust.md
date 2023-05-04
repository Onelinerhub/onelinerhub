# How to iterate an array with index in Rust
// plain

Iterating an array with index in Rust can be done using the `enumerate()` method. This method takes an iterator and returns each element of the iterator along with its index. The following example code block shows how to use `enumerate()` to iterate an array with index:

```rust
let arr = [1, 2, 3];

for (index, value) in arr.iter().enumerate() {
    println!("Index: {}, Value: {}", index, value);
}
```

The output of the above code is:

```
Index: 0, Value: 1
Index: 1, Value: 2
Index: 2, Value: 3
```

The ## Code explanation


1. `let arr = [1, 2, 3];`: This line declares an array with three elements.

2. `for (index, value) in arr.iter().enumerate()`: This line uses the `enumerate()` method to iterate the array and assign the index and value of each element to the `index` and `value` variables respectively.

3. `println!("Index: {}, Value: {}", index, value);`: This line prints the index and value of each element.

## Helpful links

- [Rust Documentation - Iterator Trait](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.enumerate)

group: rust-loops