# How to get pointer address in Rust
// plain

In Rust, you can get the address of a pointer by using the `&` operator. For example, if you have a pointer `p` pointing to a value `x`, you can get the address of `p` by using `&p`. The output of this expression will be a pointer to the address of `p`. You can also use the `std::ptr::addr` function to get the address of a pointer. This function takes a reference to a pointer and returns the address of the pointer. For example, if you have a pointer `p` pointing to a value `x`, you can get the address of `p` by using `std::ptr::addr(&p)`. The output of this expression will be a pointer to the address of `p`.

```rust
let x = 10;
let p = &x;
let address = &p;
println!("The address of p is {:p}", address);
```

### Output example

```
The address of p is 0x7ffc9f9f9f90
```

### Explanation

The `let x = 10;` statement creates a variable `x` with the value `10`. The `let p = &x;` statement creates a pointer `p` pointing to the value `x`. The `let address = &p;` statement creates a pointer `address` pointing to the address of `p`. Finally, the `println!` statement prints the address of `p` using the `{:p}` format specifier.

### Relevant links

- [Rust Reference - Pointers](https://doc.rust-lang.org/reference/pointers.html)
- [Rust Reference - Formatting](https://doc.rust-lang.org/std/fmt/index.html)
- [Rust Reference - std::ptr](https://doc.rust-lang.org/std/ptr/index.html)

group: rust-pointers