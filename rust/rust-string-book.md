# rust string book
// plain

Rust strings are a powerful data type that allow for efficient storage and manipulation of text. They are stored as a sequence of bytes, and can be manipulated with a variety of methods. The [Rust Book](https://doc.rust-lang.org/book/ch08-02-strings.html) provides a comprehensive overview of Rust strings, including how to create, manipulate, and convert them.

## Example code

```
let mut s = String::new();

s.push_str("Hello");
s.push(' ');
s.push_str("world!");

println!("{}", s);
```

## Output example

```
Hello world!
```

The code above creates a new string, `s`, and then pushes the strings "Hello" and "world!" onto it. Finally, it prints the resulting string.

The `String::new()` method creates a new, empty string. The `push_str()` method adds a string slice to the end of the string, and the `push()` method adds a single character.

## Helpful links

- [Rust Book: Strings](https://doc.rust-lang.org/book/ch08-02-strings.html)
- [Rust Strings Documentation](https://doc.rust-lang.org/std/string/index.html)