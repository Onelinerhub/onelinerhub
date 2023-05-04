# How to get index in for loop in Rust
// plain

The `for` loop in Rust is used to iterate over a collection of items. It can be used to get the index of each item in the collection. To do this, the `enumerate()` method can be used. This method takes the collection as an argument and returns a tuple containing the index and the item.

## Example code

```
let v = vec![10, 20, 30];

for (index, item) in v.enumerate() {
    println!("Index: {}, Item: {}", index, item);
}
```

## Output example

```
Index: 0, Item: 10
Index: 1, Item: 20
Index: 2, Item: 30
```

## Code explanation


1. `let v = vec![10, 20, 30];` - This line creates a vector containing the numbers 10, 20, and 30.
2. `for (index, item) in v.enumerate()` - This line starts the `for` loop. The `enumerate()` method is used to get the index and item from the vector.
3. `println!("Index: {}, Item: {}", index, item);` - This line prints the index and item for each iteration of the loop.

## Helpful links

- [Rust Documentation - For Loops](https://doc.rust-lang.org/book/ch03-03-how-functions-work.html#for-loops)
- [Rust Documentation - Enumerate](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.enumerate)

group: rust-loops