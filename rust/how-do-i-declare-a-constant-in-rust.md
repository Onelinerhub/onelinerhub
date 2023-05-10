# How do I declare a constant in Rust?
// plain

Constants in Rust are declared using the `const` keyword. The value of a constant must be known at compile time, and it cannot be changed once declared.

## Example

```
const MAX_POINTS: u32 = 100_000;
```

This declares a constant named `MAX_POINTS` of type `u32` with a value of `100_000`.

## Code explanation

- `const`: keyword used to declare a constant
- `MAX_POINTS`: name of the constant
- `u32`: type of the constant
- `100_000`: value of the constant

## Helpful links
- [Rust Documentation - Constants](https://doc.rust-lang.org/book/ch03-02-data-types.html#data-types)

group: rust-variables