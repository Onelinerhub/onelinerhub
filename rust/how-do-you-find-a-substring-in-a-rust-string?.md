# How do you find a substring in a Rust string?
// plain

You can find a substring in a Rust string using the `contains()` method. This method takes a `&str` as an argument and returns a `bool` indicating whether the string contains the substring.

## Example code

```
let my_string = "Hello World!";
let substring = "World";

let result = my_string.contains(substring);
```

## Output example

```
true
```

## Code explanation

- `let my_string = "Hello World!";`: This line declares a variable `my_string` and assigns it the value of the string `"Hello World!"`.
- `let substring = "World";`: This line declares a variable `substring` and assigns it the value of the string `"World"`.
- `let result = my_string.contains(substring);`: This line calls the `contains()` method on the `my_string` variable, passing in the `substring` variable as an argument. The result of the method is assigned to the `result` variable.

## Helpful links
- [Rust String Documentation](https://doc.rust-lang.org/std/string/struct.String.html)