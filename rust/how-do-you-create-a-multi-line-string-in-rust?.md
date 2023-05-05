# How do you create a multi-line string in Rust?
// plain

Creating a multi-line string in Rust is done using a raw string literal. A raw string literal is a string that is surrounded by two backslashes (`\`) and a pair of double quotes (`"`). The backslashes tell the compiler to ignore any special characters within the string.

## Example code

```
let my_string = r"This is a
multi-line string
in Rust";
```

## Output example

```
This is a
multi-line string
in Rust
```

## Code explanation

- `let`: This is a keyword used to declare a variable.
- `my_string`: This is the name of the variable.
- `r`: This is a prefix used to indicate a raw string literal.
- `"`: This is a double quote used to enclose the string.
- `\`: This is a backslash used to indicate that the compiler should ignore any special characters within the string.

## Helpful links
- [Rust Documentation - Strings](https://doc.rust-lang.org/book/ch08-02-strings.html)