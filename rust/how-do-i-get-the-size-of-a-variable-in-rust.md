# How do I get the size of a variable in Rust?
// plain

The size of a variable in Rust can be determined using the `std::mem::size_of` function. This function takes a reference to a type as an argument and returns the size of the type in bytes.

```rust
fn main() {
    let x = 5;
    println!("Size of x is {} bytes", std::mem::size_of::<i32>(&x));
}
```

## Output example

```
Size of x is 4 bytes
```

## Code explanation

- `std::mem::size_of`: function to determine the size of a variable in Rust
- `&x`: reference to the variable `x`
- `<i32>`: type of the variable `x`

## Helpful links
- [std::mem::size_of](https://doc.rust-lang.org/std/mem/fn.size_of.html)

group: rust-variables