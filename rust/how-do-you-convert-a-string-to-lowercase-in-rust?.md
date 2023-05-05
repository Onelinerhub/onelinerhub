# How do you convert a string to lowercase in Rust?
// plain

To convert a string to lowercase in Rust, you can use the `to_lowercase()` method. This method is part of the `String` type and is available in the `std::string` module.

## Example code

```
let my_string = "HELLO WORLD";
let my_string_lowercase = my_string.to_lowercase();
println!("{}", my_string_lowercase);
```

## Output example

```
hello world
```

## Code explanation

- `let my_string = "HELLO WORLD";`: This line declares a variable `my_string` and assigns it the value of the string `"HELLO WORLD"`.
- `let my_string_lowercase = my_string.to_lowercase();`: This line calls the `to_lowercase()` method on the `my_string` variable, and assigns the result to the `my_string_lowercase` variable.
- `println!("{}", my_string_lowercase);`: This line prints the value of the `my_string_lowercase` variable to the console.

## Helpful links
- [Rust Documentation - Strings](https://doc.rust-lang.org/std/string/index.html)