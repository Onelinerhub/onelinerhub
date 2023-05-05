# rust string append char
// plain

Rust strings are immutable, meaning that once created, they cannot be changed. However, it is possible to append a single character to a string using the `push` method.

## Example code

```
let mut s = String::from("Hello");
s.push('!');
```

## Output example

```
Hello!
```

The code above creates a mutable string `s` with the value `Hello`. The `push` method is then used to append the character `!` to the end of the string. The result is the string `Hello!`.

## Helpful links

- [Rust Strings Documentation](https://doc.rust-lang.org/std/string/struct.String.html)