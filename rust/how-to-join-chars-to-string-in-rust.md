# How to join chars to string in Rust
// plain

Joining chars to string in Rust can be done using the `collect()` method. The `collect()` method takes an iterator of type `char` and returns a `String`.

## Code example:

```
let chars = vec!['a', 'b', 'c'];
let string: String = chars.iter().collect();
```

### Output

`string` will be equal to `"abc"`

## Explanation:

- `let chars = vec!['a', 'b', 'c'];`: This line creates a vector of type `char` containing the characters `a`, `b`, and `c`.
- `let string: String =`: This line declares a variable of type `String` called `string`.
- `chars.iter()`: This line creates an iterator of type `char` from the vector `chars`.
- `.collect()`: This line collects the iterator of type `char` into a `String`.

## Helpful links:

- [Rust Documentation - Iterator](https://doc.rust-lang.org/std/iter/trait.Iterator.html)
- [Rust Documentation - Collect](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.collect)