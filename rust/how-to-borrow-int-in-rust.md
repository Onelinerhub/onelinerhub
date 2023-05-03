# How to borrow int in Rust
// plain

Rust provides the `borrow` keyword to borrow an `int` from a `struct` or `enum`. The `borrow` keyword creates a reference to the `int` that can be used to access the value without taking ownership.

## Example code

```rust
struct MyStruct {
    my_int: i32,
}

fn main() {
    let my_struct = MyStruct { my_int: 5 };
    let my_int_ref = &my_struct.my_int;
    println!("my_int_ref = {}", my_int_ref);
}
```

## Output example

```
my_int_ref = 5
```

## Code explanation

- `let my_struct = MyStruct { my_int: 5 };`: creates a `MyStruct` instance with an `int` value of `5`
- `let my_int_ref = &my_struct.my_int;`: creates a reference to the `int` value of `my_struct` using the `&` operator
- `println!("my_int_ref = {}", my_int_ref);`: prints the value of the `int` reference

## Helpful links
- [Rust Reference](https://doc.rust-lang.org/reference/index.html)
- [Rust Borrowing](https://doc.rust-lang.org/book/ch04-02-references-and-borrowing.html)

group: rust-borrow