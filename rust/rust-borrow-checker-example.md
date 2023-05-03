# Rust borrow checker example
// plain

The Rust borrow checker is a compile-time mechanism that ensures memory safety in Rust programs. It prevents data races and other memory safety issues by enforcing the borrowing rules.

## Example code

```rust
fn main() {
    let mut x = 5;
    let y = &mut x;
    *y += 1;
    println!("x = {}", x);
}
```

## Output example

```
x = 6
```

The code above shows an example of the Rust borrow checker in action. The code declares a mutable variable `x` and creates a mutable reference `y` to it. The code then attempts to modify the value of `x` through the reference `y`. The Rust borrow checker will detect this and prevent the code from compiling, as it would result in a data race.

Parts of the code:
- `let mut x = 5;`: declares a mutable variable `x` with an initial value of `5`.
- `let y = &mut x;`: creates a mutable reference `y` to `x`.
- `*y += 1;`: attempts to modify the value of `x` through the reference `y`.

## Helpful links
- [Rust Borrow Checker](https://doc.rust-lang.org/book/ch04-02-references-and-borrowing.html)

group: rust-borrow