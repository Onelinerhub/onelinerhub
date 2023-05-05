# rust string borrow
// plain

A Rust string borrow is a type of borrowing that allows a string to be used without taking ownership of it. This is done by creating a reference to the string, which can then be used to access the string's contents.

## Example code

```
let s = String::from("hello");
let s_ref = &s;
println!("{}", s_ref);
```

## Output example

```
hello
```

In the example code, the `let s = String::from("hello")` line creates a `String` object with the value "hello". The `let s_ref = &s` line creates a reference to the `String` object, which is stored in the `s_ref` variable. The `println!("{}", s_ref)` line prints out the value of the `String` object, which is "hello".

## Helpful links

- [Rust Reference](https://doc.rust-lang.org/reference/index.html)
- [Rust Strings](https://doc.rust-lang.org/std/string/index.html)