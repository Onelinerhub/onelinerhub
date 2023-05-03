# How borrow instead of move in Rust
// plain

Rust provides a powerful feature called `borrow` which allows you to access data without taking ownership of it. This is done by creating a reference to the data, which can be used to read or modify the data without taking ownership.

```rust
let mut x = 5;
let y = &x;

println!("x = {}", x);
println!("y = {}", y);
```

## Output example

```
x = 5
y = 5
```

The code above creates a mutable variable `x` and a reference `y` to `x`. The reference `y` can be used to access the value of `x` without taking ownership of it.

The following ## Code explanation


- `let mut x = 5;`: This creates a mutable variable `x` with the value `5`.
- `let y = &x;`: This creates a reference `y` to the variable `x`.
- `println!("x = {}", x);`: This prints the value of `x` to the console.
- `println!("y = {}", y);`: This prints the value of `y` to the console.

For more information about borrowing in Rust, please refer to the [Rust Book](https://doc.rust-lang.org/book/ch04-02-references-and-borrowing.html).

group: rust-borrow