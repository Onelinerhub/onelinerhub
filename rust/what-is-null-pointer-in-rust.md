# What is null pointer in Rust
// plain

A null pointer in Rust is a pointer that does not point to any valid object. It is represented by the type `std::ptr::null()`. It is used to indicate that a pointer is not pointing to a valid object.

## Example code

```
let ptr: *const i32 = std::ptr::null();
```

## Output example

```
ptr: *const i32 = 0x0
```

## Code explanation

- `let ptr: *const i32`: declares a pointer `ptr` of type `*const i32`
- `std::ptr::null()`: returns a null pointer of type `*const T`

## Helpful links
- [Rust Documentation - std::ptr](https://doc.rust-lang.org/std/ptr/)

group: rust-null