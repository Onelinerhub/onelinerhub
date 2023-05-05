# rust string buffer
// plain

A Rust String Buffer is a type of data structure used to store and manipulate strings. It is similar to a vector in that it can grow and shrink dynamically, but it is specifically designed to store strings. It is also optimized for efficient string manipulation, such as concatenation, slicing, and searching.

## Example code

```
let mut s = String::new();
s.push_str("Hello");
s.push_str(" World!");
println!("{}", s);
```

## Output example

```
Hello World!
```

## Code explanation

- `let mut s = String::new();`: This line creates a new empty string buffer.
- `s.push_str("Hello");`: This line adds the string "Hello" to the end of the string buffer.
- `s.push_str(" World!");`: This line adds the string " World!" to the end of the string buffer.
- `println!("{}", s);`: This line prints the contents of the string buffer to the console.

## Helpful links
- [Rust String Buffer Documentation](https://doc.rust-lang.org/std/string/struct.String.html)