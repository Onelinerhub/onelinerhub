# How do I reverse a string in Rust?
// plain

Reversing a string in Rust is a simple task that can be accomplished with the `.chars().rev()` method. This method returns an iterator that yields the characters of the string in reverse order.

```rust
let s = "Hello World";
let reversed = s.chars().rev().collect::<String>();
println!("{}", reversed);
```

## Output example

```
dlroW olleH
```

The code above consists of the following parts:

1. `let s = "Hello World";` - This line declares a variable `s` and assigns it the value of the string `"Hello World"`.

2. `let reversed = s.chars().rev().collect::<String>();` - This line uses the `.chars()` method to convert the string `s` into an iterator of characters, then uses the `.rev()` method to reverse the order of the characters, and finally uses the `.collect()` method to collect the reversed characters into a new string.

3. `println!("{}", reversed);` - This line prints the reversed string to the console.

## Helpful links

- [Rust Documentation - Strings](https://doc.rust-lang.org/std/string/struct.String.html)
- [Rust Documentation - Iterators](https://doc.rust-lang.org/std/iter/trait.Iterator.html)