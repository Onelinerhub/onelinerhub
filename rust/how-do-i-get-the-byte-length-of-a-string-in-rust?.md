# How do I get the byte length of a string in Rust?
// plain

The byte length of a string in Rust can be obtained using the `len()` method. This method returns the number of bytes in the string.

## Example code

```
let s = "Hello world!";
let len = s.len();
println!("The length of '{}' is {} bytes.", s, len);
```

## Output example

```
The length of 'Hello world!' is 12 bytes.
```

## Code explanation

- `let s = "Hello world!";`: This line declares a string variable `s` and assigns it the value `"Hello world!"`.
- `let len = s.len();`: This line calls the `len()` method on the `s` string variable and assigns the result to the `len` variable.
- `println!("The length of '{}' is {} bytes.", s, len);`: This line prints the length of the `s` string variable to the console.

## Helpful links
- [String::len()](https://doc.rust-lang.org/std/string/struct.String.html#method.len)