# How to enumerate a slice in Rust?
// plain

Enumerating a slice in Rust is a simple process. To do so, you can use the `enumerate()` method on the slice. This method returns a tuple containing the index and the value of each element in the slice.

```rust
let numbers = [1, 2, 3];

for (index, value) in numbers.enumerate() {
    println!("Index: {}, Value: {}", index, value);
}
```

## Output example

```
Index: 0, Value: 1
Index: 1, Value: 2
Index: 2, Value: 3
```

The code above consists of the following parts:

- `let numbers = [1, 2, 3];`: This line declares a slice of numbers.
- `for (index, value) in numbers.enumerate()`: This line uses the `enumerate()` method to enumerate the slice. It returns a tuple containing the index and the value of each element in the slice.
- `println!("Index: {}, Value: {}", index, value);`: This line prints the index and the value of each element in the slice.

## Helpful links

- [Rust Documentation - Enumerate](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.enumerate)

group: rust-slice