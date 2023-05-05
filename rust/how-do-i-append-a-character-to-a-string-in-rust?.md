# How do I append a character to a string in Rust?
// plain

You can append a character to a string in Rust using the `push()` method. This method takes a single character as an argument and adds it to the end of the string.

```rust
let mut s = String::from("Hello");
s.push('!');
println!("{}", s);
```

## Output example

```
Hello!
```

The code above does the following:

1. Declares a mutable string `s` and assigns it the value `Hello`.
2. Calls the `push()` method on `s` with the argument `!`.
3. Prints the value of `s` to the console.

## Helpful links

- [String::push()](https://doc.rust-lang.org/std/string/struct.String.html#method.push)