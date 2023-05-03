# How to borrow moved value in Rust
// plain

Rust provides a powerful feature called "move semantics" which allows you to move values from one place to another without copying them. This can be useful when dealing with large data structures or when you want to avoid unnecessary copying.

```rust
let mut x = vec![1, 2, 3];
let y = x;

println!("x = {:?}", x);
```

## Output example

```
x = []
```

In the example above, the value of `x` is moved to `y`, leaving `x` with an empty vector.

To borrow the moved value, you can use the `ref` keyword. This will create a reference to the moved value, allowing you to access it without copying it.

```rust
let mut x = vec![1, 2, 3];
let y = &x;

println!("x = {:?}", x);
```

## Output example

```
x = [1, 2, 3]
```

## Code explanation

- `let mut x = vec![1, 2, 3];`: creates a mutable vector with the values 1, 2, and 3.
- `let y = x;`: moves the value of `x` to `y`.
- `let y = &x;`: creates a reference to the moved value of `x`.

## Helpful links
- [Rust Move Semantics](https://doc.rust-lang.org/book/ch15-01-box.html#move-semantics)
- [Rust Reference](https://doc.rust-lang.org/book/ch04-02-references-and-borrowing.html#references-and-borrowing)

group: rust-borrow