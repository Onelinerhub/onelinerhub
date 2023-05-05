# How do I get a character from a string in Rust by its index?
// plain

You can get a character from a string in Rust by its index using the `chars()` method. This method returns an iterator over the characters of a string.

## Example code

```
let s = "Hello";
let c = s.chars().nth(1);
```

## Output example

```
Some('e')
```

## Code explanation

- `let s = "Hello"`: This declares a string variable `s` and assigns it the value `"Hello"`.
- `let c = s.chars().nth(1)`: This uses the `chars()` method to get an iterator over the characters of the string `s`. The `nth(1)` method is then used to get the character at the index `1` from the iterator.

## Helpful links
- [String::chars()](https://doc.rust-lang.org/std/string/struct.String.html#method.chars)
- [Iterator::nth()](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.nth)