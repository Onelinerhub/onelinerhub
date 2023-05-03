# How to free box memory in Rust
// plain

Rust provides a number of ways to free memory.

1. Drop: The `drop` function is used to free memory associated with a variable. It is called automatically when a variable goes out of scope.

```rust
let x = Box::new(5);
drop(x);
```

2. Manually: Memory can also be manually freed using the `std::mem::drop` function.

```rust
let x = Box::new(5);
std::mem::drop(x);
```

3. `std::mem::forget`: The `std::mem::forget` function can be used to manually free memory without calling the `drop` function.

```rust
let x = Box::new(5);
std::mem::forget(x);
```

4. `std::mem::replace`: The `std::mem::replace` function can be used to replace a variable with a new value and free the memory associated with the old value.

```rust
let mut x = Box::new(5);
std::mem::replace(&mut x, Box::new(6));
```

5. `std::mem::swap`: The `std::mem::swap` function can be used to swap two variables and free the memory associated with the old values.

```rust
let mut x = Box::new(5);
let mut y = Box::new(6);
std::mem::swap(&mut x, &mut y);
```

These functions can be used to free memory in Rust.

group: rust-box