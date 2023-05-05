# How do I get the last character from a string in Rust?
// plain

The easiest way to get the last character from a string in Rust is to use the `chars()` method. This method returns an iterator over the characters of a string. To get the last character, we can use the `last()` method on the iterator.

```rust
let s = "Hello";
let last_char = s.chars().last().unwrap();
println!("The last character of {} is {}", s, last_char);
```

## Output example

```
The last character of Hello is o
```

## Code explanation

- `let s = "Hello"`: This line declares a string variable `s` and assigns it the value `"Hello"`.
- `let last_char = s.chars().last().unwrap()`: This line uses the `chars()` method to get an iterator over the characters of the string `s`. The `last()` method is then used to get the last character from the iterator. The `unwrap()` method is used to get the character from the `Option` type returned by `last()`.
- `println!("The last character of {} is {}", s, last_char)`: This line prints the last character of the string `s`.

## Helpful links
- [String](https://doc.rust-lang.org/std/string/struct.String.html)
- [chars()](https://doc.rust-lang.org/std/primitive.str.html#method.chars)
- [last()](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.last)
- [unwrap()](https://doc.rust-lang.org/std/option/enum.Option.html#method.unwrap)