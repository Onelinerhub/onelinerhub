# How do I capitalize a string in Rust?
// plain

To capitalize a string in Rust, you can use the `to_uppercase()` method. This method is available on all `String` types.

## Example code

```
let my_string = "hello world";
let my_string_uppercase = my_string.to_uppercase();
```

## Output example

```
HELLO WORLD
```

The code above takes a string, `my_string`, and calls the `to_uppercase()` method on it. This returns a new string, `my_string_uppercase`, which is the original string with all characters capitalized.

Parts of the code:
- `let my_string = "hello world";`: This declares a variable, `my_string`, and assigns it the value of the string `"hello world"`.
- `let my_string_uppercase = my_string.to_uppercase();`: This calls the `to_uppercase()` method on the `my_string` variable, and assigns the result to the `my_string_uppercase` variable.

## Helpful links
- [Rust Documentation - Strings](https://doc.rust-lang.org/std/string/struct.String.html)