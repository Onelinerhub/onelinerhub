# How do I replace all strings in Rust?
// plain

Replacing strings in Rust is a common task and can be done using the `replace` method. This method takes two parameters, the string to be replaced and the string to replace it with. For example:

```rust
let my_string = "Hello World!";
let new_string = my_string.replace("World", "Rust");
println!("{}", new_string);
```

## Output example

```
Hello Rust!
```

The `replace` method takes two parameters:

1. The string to be replaced (`"World"` in the example above)
2. The string to replace it with (`"Rust"` in the example above)

Alternatively, you can also use the `replace_all` method, which takes a regular expression as the first parameter and a string as the second parameter. This method will replace all occurrences of the regular expression with the given string.

## Helpful links

- [Rust Documentation - Strings](https://doc.rust-lang.org/std/string/index.html)
- [Rust Documentation - Strings - replace](https://doc.rust-lang.org/std/string/struct.String.html#method.replace)
- [Rust Documentation - Strings - replace_all](https://doc.rust-lang.org/std/string/struct.String.html#method.replace_all)