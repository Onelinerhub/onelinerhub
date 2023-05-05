# rust string copy
// plain

A Rust `String` can be copied using the `clone()` method. This method creates a new `String` with the same contents as the original.

## Example

```
let s1 = String::from("Hello World!");
let s2 = s1.clone();

println!("s1 = {}, s2 = {}", s1, s2);
```

## Output example

```
s1 = Hello World!, s2 = Hello World!
```

The `clone()` method:
- Creates a new `String` with the same contents as the original.
- Allocates memory for the new `String` on the heap.
- Copies the contents of the original `String` into the new `String`.

## Helpful links
- [Rust Documentation - String](https://doc.rust-lang.org/std/string/struct.String.html)