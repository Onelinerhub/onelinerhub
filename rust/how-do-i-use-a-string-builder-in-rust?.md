# How do I use a String Builder in Rust?
// plain

String Builder is a type of data structure used to efficiently build strings in Rust. It is used to create a mutable string that can be modified in place.

## Example code

```
let mut s = String::new();
let mut sb = String::new();

sb.push_str("Hello");
sb.push_str(" World!");

s.push_str(&sb);

println!("{}", s);
```

## Output example

```
Hello World!
```

## Code explanation

- `let mut s = String::new();`: creates a new empty string
- `let mut sb = String::new();`: creates a new empty string builder
- `sb.push_str("Hello");`: adds the string "Hello" to the string builder
- `sb.push_str(" World!");`: adds the string " World!" to the string builder
- `s.push_str(&sb);`: adds the contents of the string builder to the string
- `println!("{}", s);`: prints the contents of the string

## Helpful links
- [Rust Documentation - String Builder](https://doc.rust-lang.org/std/string/struct.String.html#method.push_str)