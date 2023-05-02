# How to filter a vector of strings in Rust
// plain

To filter a vector of strings in Rust, you can use the `filter()` method. This method takes a closure as an argument, which is used to determine which elements of the vector should be kept. The closure should return a boolean value, with `true` indicating that the element should be kept and `false` indicating that it should be discarded. For example, the following code will filter a vector of strings to only include strings that are longer than 5 characters:
```rust
let strings = vec!["foo", "bar", "baz", "quux"];
let filtered_strings = strings.filter(|s| s.len() > 5);
```
The output of this code will be a vector containing only the strings `"baz"` and `"quux"`.

For more information on the `filter()` method, see the [Rust documentation](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.filter). Additionally, the [Rust by Example](https://doc.rust-lang.org/rust-by-example/iter/filter.html) page provides a more detailed example of how to use the `filter()` method.