# How do I print the address of a variable in Rust?
// plain

You can print the address of a variable in Rust using the `std::ptr::addr_of` function. This function takes a reference to a variable as an argument and returns the address of the variable as a `*const T` pointer.

## Example code

```rust
let x = 5;
let x_addr = std::ptr::addr_of(&x);
println!("x is at address {:p}", x_addr);
```

## Output example

```
x is at address 0x7ffc9f9f9f90
```

## Code explanation

- `let x = 5;`: Declares a variable `x` with the value `5`.
- `let x_addr = std::ptr::addr_of(&x);`: Calls the `std::ptr::addr_of` function with a reference to `x` as an argument, and assigns the address of `x` to the `x_addr` variable.
- `println!("x is at address {:p}", x_addr);`: Prints the address of `x` using the `{:p}` format specifier.

## Helpful links
- [std::ptr::addr_of](https://doc.rust-lang.org/std/ptr/fn.addr_of.html)

group: rust-variables