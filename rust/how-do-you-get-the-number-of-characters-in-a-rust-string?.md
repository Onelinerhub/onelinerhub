# How do you get the number of characters in a Rust string?
// plain

You can get the number of characters in a Rust string using the `len()` method. This method returns the length of the string as an `usize` type.

## Example code

```rust
let my_string = "Hello World!";
let length = my_string.len();
println!("The length of '{}' is {}.", my_string, length);
```

## Output example

```
The length of 'Hello World!' is 12.
```

## Code explanation

- `let my_string = "Hello World!";`: This line declares a string variable `my_string` and assigns it the value `"Hello World!"`.
- `let length = my_string.len();`: This line calls the `len()` method on the `my_string` variable and assigns the result to the `length` variable.
- `println!("The length of '{}' is {}.", my_string, length);`: This line prints the length of the string to the console.

## Helpful links
- [Rust String Documentation](https://doc.rust-lang.org/std/string/struct.String.html)