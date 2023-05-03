# Rust unsafe borrow example
// plain

An example of an unsafe borrow in Rust is when a reference to a value is used after that value has been dropped. This can lead to a segmentation fault or other undefined behavior.

```
let mut x = 5;
let y = &mut x;
drop(x);
println!("{}", y);
```

## Output example

```
thread 'main' panicked at 'already borrowed: BorrowMutError', src/libcore/result.rs:1165:5
```

## Code explanation

- `let mut x = 5;`: Declares a mutable variable `x` with the value `5`.
- `let y = &mut x;`: Creates a mutable reference `y` to `x`.
- `drop(x);`: Drops the value of `x`.
- `println!("{}", y);`: Attempts to print the value of `y`, which is a reference to `x` that has already been dropped.

## Helpful links
- [Rust Reference](https://doc.rust-lang.org/reference/index.html)
- [Rust Borrowing Rules](https://doc.rust-lang.org/book/ch04-02-references-and-borrowing.html#the-rules-of-references)

group: rust-borrow