# rust string capitalize
// plain

Rust strings can be capitalized using the `to_uppercase()` method. This method returns a new string with all characters in uppercase.

## Example

```
let s = "hello world";
let uppercase = s.to_uppercase();
println!("{}", uppercase);
```
## Output example

```
HELLO WORLD
```

The `to_uppercase()` method takes no parameters and is part of the `std::string::String` type. It is a mutable method, meaning it changes the string in place.

## Code explanation

- `let s = "hello world"`: This line declares a string variable `s` and assigns it the value `"hello world"`.
- `let uppercase = s.to_uppercase()`: This line calls the `to_uppercase()` method on the `s` string variable, and assigns the result to the `uppercase` variable.
- `println!("{}", uppercase)`: This line prints the value of the `uppercase` variable to the console.

## Helpful links
- [Rust Strings Documentation](https://doc.rust-lang.org/std/string/struct.String.html)