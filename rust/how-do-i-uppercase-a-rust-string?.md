# How do I uppercase a Rust string?
// plain

To uppercase a Rust string, you can use the `to_uppercase()` method. This method is available on all `String` types.

## Example

```
let my_string = "hello world";
let uppercase_string = my_string.to_uppercase();
```

## Output example

```
HELLO WORLD
```

The `to_uppercase()` method takes no arguments and returns a new `String` with all characters in uppercase.

## Code explanation

- `let my_string = "hello world";`: This line declares a `String` variable called `my_string` and assigns it the value `"hello world"`.
- `let uppercase_string = my_string.to_uppercase();`: This line calls the `to_uppercase()` method on the `my_string` variable and assigns the result to a new `String` variable called `uppercase_string`.

## Helpful links
- [Rust String Documentation](https://doc.rust-lang.org/std/string/struct.String.html)