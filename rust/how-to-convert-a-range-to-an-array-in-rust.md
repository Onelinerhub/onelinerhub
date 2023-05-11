# How to convert a range to an array in Rust?
// plain

To convert a range to an array in Rust, you can use the `collect()` method. This method takes an iterator and collects its elements into a collection. For example, the following code will convert a range from 0 to 10 into an array:

```rust
let range = 0..10;
let array: Vec<i32> = range.collect();
```

The output of this code will be an array of type `Vec<i32>` containing the elements from 0 to 10:

```
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

The code consists of the following parts:

- `let range = 0..10;`: This line declares a range from 0 to 10.
- `let array: Vec<i32> = range.collect();`: This line uses the `collect()` method to convert the range into an array of type `Vec<i32>`.

For more information, see the [Rust documentation](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.collect).