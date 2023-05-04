# How to check a value for null in Rust
// plain

To check a value for null in Rust, you can use the `Option` type. `Option` is an enum with two variants: `Some` and `None`. `Some` is used to wrap a value, while `None` is used to indicate the absence of a value.

## Example code

```rust
let x: Option<i32> = Some(5);

match x {
    Some(i) => println!("x is {}", i),
    None => println!("x is None"),
}
```

## Output example

```
x is 5
```

## Code explanation

- `let x: Option<i32> = Some(5);`: This line declares a variable `x` of type `Option<i32>` and assigns it the value `Some(5)`.
- `match x {`: This line starts a `match` expression, which is used to compare a value against a list of patterns and execute code based on which pattern matches.
- `Some(i) => println!("x is {}", i)`: This line is a pattern that matches the `Some` variant of the `Option` type. If this pattern matches, the code `println!("x is {}", i)` is executed, where `i` is the value wrapped in the `Some` variant.
- `None => println!("x is None")`: This line is a pattern that matches the `None` variant of the `Option` type. If this pattern matches, the code `println!("x is None")` is executed.

## Helpful links
- [Rust Book - Match](https://doc.rust-lang.org/book/ch06-02-match.html)
- [Rust Book - Option](https://doc.rust-lang.org/book/ch06-01-working-with-generic-types.html#using-generic-types-traits-and-lifetimes-in-function-definitions)

group: rust-null