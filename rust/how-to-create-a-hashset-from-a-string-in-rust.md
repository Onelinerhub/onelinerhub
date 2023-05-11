# How to create a HashSet from a String in Rust?
// plain

A `HashSet` is a data structure in Rust that stores unique values. It can be created from a `String` using the `FromIterator` trait.

```rust
let my_string = "Hello World";
let my_set: HashSet<&str> = my_string.split_whitespace().collect();
```

The output of the above code is:
```
{"Hello", "World"}
```

The code works by first splitting the `String` into an iterator of `&str` using `split_whitespace()`. This iterator is then collected into a `HashSet` using the `collect()` method.

The relevant parts of the code are:
- `my_string`: a `String` containing the text to be converted to a `HashSet`
- `split_whitespace()`: a method that splits a `String` into an iterator of `&str`
- `collect()`: a method that collects an iterator into a `HashSet`

## Helpful links
- [Rust Docs - HashSet](https://doc.rust-lang.org/std/collections/struct.HashSet.html)
- [Rust Docs - FromIterator](https://doc.rust-lang.org/std/iter/trait.FromIterator.html)

group: hashset

onelinerhub: [How to create a HashSet from a String in Rust?](https://onelinerhub.com/rust/how-to-create-a-hashset-from-a-string-in-rust)