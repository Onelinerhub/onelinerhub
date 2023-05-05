# How to get the length of a string in Rust?
// plain

The length of a string in Rust can be obtained using the `len()` method. This method returns the length of the string as a `usize` type.

## Example code

```
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
- `let length = my_string.len();`: This line calls the `len()` method on the `my_string` variable and assigns the returned value to the `length` variable.
- `println!("The length of '{}' is {}.", my_string, length);`: This line prints the length of the string to the console.

## Helpful links
- [Rust Documentation - Strings](https://doc.rust-lang.org/std/string/struct.String.html)