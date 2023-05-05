# What is the maximum size of a string in Rust?
// plain

The maximum size of a string in Rust is determined by the amount of memory available. A string in Rust is a collection of Unicode scalar values encoded as a stream of UTF-8 bytes. The maximum size of a string is usize, which is the size of the machine's pointer.

## Example code

```
let s = String::with_capacity(usize::MAX);
```

## Output example

```
Compiling playground v0.0.1 (/playground)
error[E0015]: calls in constants are limited to constant functions, tuple structs and tuple variants
 --> src/main.rs:1:25
  |
1 |     let s = String::with_capacity(usize::MAX);
  |                         ^^^^^^^^^^^^
  |
  = note: `usize::MAX` is not a constant function

error: aborting due to previous error

For more information about this error, try `rustc --explain E0015`.
```

The code above is trying to create a string with the maximum size of usize, which is not allowed in Rust.

## Code explanation


- `let s =`: This is a variable declaration, declaring a variable named `s`.
- `String::with_capacity(usize::MAX)`: This is a method call on the `String` type, attempting to create a string with the maximum size of `usize`.
- `usize::MAX`: This is a constant representing the maximum size of `usize`.

## Helpful links

- [Rust Strings](https://doc.rust-lang.org/std/string/struct.String.html)
- [Rust usize](https://doc.rust-lang.org/std/primitive.usize.html)