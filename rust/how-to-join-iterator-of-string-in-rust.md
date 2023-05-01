# How to join iterator of string in Rust
// plain

Joining an iterator of strings in Rust can be done using the `join` method of the `std::iter::Iterator` trait. This method takes a single argument, which is the separator string to be used between each string in the iterator. The following ## Code example shows how to join an iterator of strings using the `join` method:

```rust
let strings = vec!["Hello", "World", "!"];
let joined_string = strings.iter().join(", ");

println!("{}", joined_string);
```

### Output
```
Hello, World, !
```

Explanation:
- `let strings = vec!["Hello", "World", "!"];`: This line creates a vector of strings containing the elements "Hello", "World" and "!".
- `let joined_string = strings.iter().join(", ");`: This line uses the `join` method of the `std::iter::Iterator` trait to join the strings in the vector with the separator string ", ".
- `println!("{}", joined_string);`: This line prints the joined string to the console.

## Helpful links:
- [std::iter::Iterator::join](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.join)
- [Rust Iterators](https://doc.rust-lang.org/book/ch13-02-iterators.html)