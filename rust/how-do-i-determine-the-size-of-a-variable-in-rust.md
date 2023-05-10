# How do I determine the size of a variable in Rust?
// plain

The size of a variable in Rust can be determined using the `std::mem::size_of` function. This function takes a reference to a type and returns the size of the type in bytes.

```rust
fn main() {
    let x = 5;
    println!("Size of x is {} bytes", std::mem::size_of_val(&x));
}
```

## Output example

```
Size of x is 8 bytes
```

The code above has the following parts:

- `let x = 5`: This declares a variable `x` with the value `5`.
- `std::mem::size_of_val(&x)`: This calls the `std::mem::size_of_val` function, which takes a reference to a type and returns the size of the type in bytes.
- `println!("Size of x is {} bytes", std::mem::size_of_val(&x))`: This prints the size of the variable `x` in bytes.

## Helpful links

- [std::mem::size_of](https://doc.rust-lang.org/std/mem/fn.size_of.html)

group: rust-variables