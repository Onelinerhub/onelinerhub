# rust string byte length
// plain

The byte length of a Rust string can be determined using the `.len()` method. This method returns the number of bytes in the string.

## Example

```
let my_string = "Hello World!";
let byte_length = my_string.len();
println!("The byte length of '{}' is {}", my_string, byte_length);
```
## Output example

```
The byte length of 'Hello World!' is 12
```

The `.len()` method is part of the `std::string::String` type. It takes no arguments and returns the number of bytes in the string.

## Helpful links
- [Rust Documentation - Strings](https://doc.rust-lang.org/std/string/struct.String.html)