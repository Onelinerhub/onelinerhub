# How to do a for loop with index in Rust
// plain

A `for` loop with index in Rust can be used to iterate over a collection of items and access the index of each item. The `enumerate()` method can be used to get the index of each item in the collection.

## Example code

```
let v = vec![10, 20, 30];

for (index, value) in v.iter().enumerate() {
    println!("Index: {}, Value: {}", index, value);
}
```

## Output example

```
Index: 0, Value: 10
Index: 1, Value: 20
Index: 2, Value: 30
```

## Code explanation

- `let v = vec![10, 20, 30];`: This line creates a vector `v` with three elements.
- `for (index, value) in v.iter().enumerate()`: This line starts a `for` loop that iterates over the vector `v` and assigns the index of each item to the variable `index` and the value of each item to the variable `value`.
- `println!("Index: {}, Value: {}", index, value);`: This line prints the index and value of each item in the vector.

## Helpful links
- [Rust Documentation - Iterators](https://doc.rust-lang.org/stable/book/ch13-02-iterators.html)
- [Rust Documentation - Enumerate](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.enumerate)

group: rust-loops