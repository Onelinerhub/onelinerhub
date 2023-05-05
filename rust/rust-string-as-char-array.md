# rust string as char array
// plain

A Rust `String` can be converted to a `char` array using the `.chars()` method. This method returns an iterator over the characters of the string.

## Example code

```rust
let my_string = "Hello World!";
let char_array: Vec<char> = my_string.chars().collect();
```

## Output example

```
[ 'H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd', '!' ]
```

## Code explanation

- `let my_string = "Hello World!";`: This line declares a `String` variable called `my_string` and assigns it the value `"Hello World!"`.
- `let char_array: Vec<char> = my_string.chars().collect();`: This line declares a `Vec<char>` variable called `char_array` and assigns it the result of the `.chars()` method called on `my_string`. The `.chars()` method returns an iterator over the characters of the string, and the `.collect()` method collects the iterator into a `Vec<char>`.

## Helpful links
- [Rust Documentation - Strings](https://doc.rust-lang.org/std/string/struct.String.html)
- [Rust Documentation - Iterators](https://doc.rust-lang.org/std/iter/index.html)
- [Rust Documentation - Vectors](https://doc.rust-lang.org/std/vec/index.html)