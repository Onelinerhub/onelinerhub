# How do I use a String Buffer in Rust?
// plain

String Buffer is a type of data structure used to store and manipulate strings in Rust. It is similar to a vector, but instead of storing elements of any type, it stores characters.

## Example code

```
let mut s = String::new();
let mut s_buf = String::with_capacity(10);

s_buf.push_str("Hello");
s_buf.push(' ');
s_buf.push_str("World!");

s.push_str(&s_buf);

println!("{}", s);
```

## Output example

```
Hello World!
```

## Code explanation

- `let mut s = String::new();`: creates a new empty string
- `let mut s_buf = String::with_capacity(10);`: creates a new string buffer with capacity of 10
- `s_buf.push_str("Hello");`: pushes the string "Hello" into the string buffer
- `s_buf.push(' ');`: pushes a single character ' ' into the string buffer
- `s_buf.push_str("World!");`: pushes the string "World!" into the string buffer
- `s.push_str(&s_buf);`: pushes the contents of the string buffer into the string
- `println!("{}", s);`: prints the contents of the string

## Helpful links
- [Rust String Buffer Documentation](https://doc.rust-lang.org/std/string/struct.String.html)