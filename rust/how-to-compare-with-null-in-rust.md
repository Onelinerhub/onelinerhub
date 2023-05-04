# How to compare with null in Rust
// plain

Comparing with `null` in Rust is done using the `Option` enum. `Option` is an enum with two variants, `Some` and `None`. `Some` is used to wrap a value, while `None` is used to represent the absence of a value.

## Example code

```rust
let x = Some(5);
let y = None;

match x {
    Some(i) => println!("x is {}", i),
    None => println!("x is None"),
}

match y {
    Some(i) => println!("y is {}", i),
    None => println!("y is None"),
}
```

## Output example

```
x is 5
y is None
```

## Code explanation


1. `let x = Some(5);`: This line declares a variable `x` and assigns it the value `Some(5)`. `Some` is a variant of the `Option` enum, and it wraps the value `5`.
2. `let y = None;`: This line declares a variable `y` and assigns it the value `None`. `None` is a variant of the `Option` enum, and it represents the absence of a value.
3. `match x {`: This line starts a `match` expression, which is used to compare the value of `x` with the variants of the `Option` enum.
4. `Some(i) => println!("x is {}", i),`: This line is a `match` arm, and it is used to handle the case where `x` is equal to `Some`. The value wrapped by `Some` is assigned to the variable `i`, and then it is printed.
5. `None => println!("x is None"),`: This line is a `match` arm, and it is used to handle the case where `x` is equal to `None`. It prints a message indicating that `x` is `None`.

## Helpful links

- [Rust Book - Match](https://doc.rust-lang.org/book/ch06-02-match.html)
- [Rust Book - Option](https://doc.rust-lang.org/book/ch06-01-working-with-types.html#the-option-enum)

group: rust-null