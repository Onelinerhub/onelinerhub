# How do you check if a Rust string ends with a certain character?
// plain

You can check if a Rust string ends with a certain character by using the `ends_with()` method. This method takes a single character as an argument and returns a boolean value.

## Example code

```
let my_string = "Hello World!";
let result = my_string.ends_with('!');
```

## Output example

```
true
```

## Code explanation

- `let my_string = "Hello World!";`: This line declares a string variable called `my_string` and assigns it the value `Hello World!`.
- `let result = my_string.ends_with('!');`: This line calls the `ends_with()` method on the `my_string` variable, passing in the character `!` as an argument. The result of the method is stored in the `result` variable.
- `true`: This is the output of the example code, indicating that the string `Hello World!` does indeed end with the character `!`.

## Helpful links
- [Rust Documentation - Strings](https://doc.rust-lang.org/std/string/struct.String.html)