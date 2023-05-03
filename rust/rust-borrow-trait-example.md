# Rust borrow trait example
// plain

The Rust `Borrow` trait is a trait that allows a type to borrow data from another type. It is used to provide a safe way to access data without taking ownership of it.

## Example code

```rust
fn main() {
    let a = String::from("Hello");
    let b = a.borrow();
    println!("{}", b);
}
```

## Output example

```
Hello
```

The code above shows an example of using the `Borrow` trait. The `a` variable is created with a `String` value. The `b` variable is then created by borrowing the data from `a` using the `borrow()` method. The `println!` statement then prints the value of `b`, which is the same as the value of `a`.

The `Borrow` trait is useful for accessing data without taking ownership of it. This allows the data to be used without having to worry about ownership issues.

## Helpful links

- [Rust Documentation - Borrow](https://doc.rust-lang.org/std/borrow/trait.Borrow.html)

group: rust-borrow