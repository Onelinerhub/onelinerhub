# How do you enumerate a Rust string?
// plain

A Rust string can be enumerated using the `chars()` method. This method returns an iterator over the characters of the string.

```rust
let s = "Hello World";

for c in s.chars() {
    println!("{}", c);
}
```

## Output example

```
H
e
l
l
o

W
o
r
l
d
```

The `chars()` method returns an iterator over the characters of the string. The iterator can then be used to iterate over the characters of the string. In the example above, the iterator is used in a for loop to print out each character of the string.

## Helpful links

- [Rust Documentation - Strings](https://doc.rust-lang.org/std/string/struct.String.html)