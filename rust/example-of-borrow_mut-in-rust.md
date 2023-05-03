# Example of borrow_mut in Rust
// plain

`Borrow_mut` is a Rust language feature that allows a mutable reference to be taken from a data structure. This allows the data structure to be modified without taking ownership of it.

## Example code

```
let mut x = vec![1, 2, 3];
let y = &mut x;
y.push(4);
```

## Output example

```
[1, 2, 3, 4]
```

## Code explanation

- `let mut x = vec![1, 2, 3];`: This line creates a mutable vector `x` with the values `1`, `2`, and `3`.
- `let y = &mut x;`: This line creates a mutable reference `y` to the vector `x`.
- `y.push(4);`: This line adds the value `4` to the vector `x` using the mutable reference `y`.

## Helpful links
- [Rust Reference - Borrow_mut](https://doc.rust-lang.org/reference/expressions/operator-expr.html#borrow-mut)

group: rust-borrow