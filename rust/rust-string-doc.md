# rust string doc
// plain

Rust strings are a collection of bytes, and are used to represent text. Strings are immutable, meaning that once created, their contents cannot be changed. The [Rust String Docs](https://doc.rust-lang.org/std/string/struct.String.html) provide detailed information about the various methods and operations that can be performed on strings.

## Example


```rust
let mut s = String::from("Hello");

s.push_str(", world!");

println!("{}", s);
```

## Output example


```
Hello, world!
```

The example above creates a `String` called `s` and assigns it the value `Hello`. The `push_str()` method is then used to append the string `", world!"` to the end of `s`. Finally, the `println!` macro is used to print the contents of `s` to the console.

The Rust String Docs provide information about the following methods and operations:

- Creating strings
- Appending strings
- Comparing strings
- Slicing strings
- Iterating over strings
- Formatting strings
- Converting strings to other types
- Encoding and decoding strings
- Searching strings
- Replacing strings
- Trimming strings
- Joining strings
- Splitting strings
- Copying strings
- Reversing strings
- Counting characters
- Comparing characters
- Converting characters
- Encoding and decoding characters
- Iterating over characters
- Parsing characters

## Helpful links

- [Rust String Docs](https://doc.rust-lang.org/std/string/struct.String.html)