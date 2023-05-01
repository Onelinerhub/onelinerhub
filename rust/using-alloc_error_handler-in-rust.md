# Using alloc_error_handler in Rust
// plain

The `alloc_error_handler` function in Rust is used to set a custom error handler for memory allocation errors. This allows you to customize the behavior of the program when an allocation error occurs.

Here is an example of how to use `alloc_error_handler`:

```rust
use std::alloc::{alloc_error_handler, Layout};

fn my_error_handler(_: Layout) -> ! {
    panic!("allocation error!");
}

fn main() {
    alloc_error_handler(my_error_handler);
    // ...
}
```

This code will set the custom error handler `my_error_handler` to be called when an allocation error occurs. The `my_error_handler` function will panic with the message "allocation error!".

Explanation of code parts:

1. `use std::alloc::{alloc_error_handler, Layout};`: This imports the `alloc_error_handler` and `Layout` functions from the `std::alloc` module.

2. `fn my_error_handler(_: Layout) -> ! { panic!("allocation error!"); }`: This defines a custom error handler function that takes a `Layout` argument and returns `!` (never returns). The function will panic with the message "allocation error!" when called.

3. `alloc_error_handler(my_error_handler);`: This sets the custom error handler `my_error_handler` to be called when an allocation error occurs.

## Helpful links:

1. [Rust alloc_error_handler documentation](https://doc.rust-lang.org/std/alloc/fn.alloc_error_handler.html)
2. [Rust alloc module documentation](https://doc.rust-lang.org/std/alloc/)