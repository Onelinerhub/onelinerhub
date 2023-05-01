# How to downcast an error in Rust
// plain

Downcasting an error in Rust is done using the `try_downcast_ref` method from the `std::error::Error` trait. This method takes a reference to an `Error` trait object and attempts to downcast it to a concrete type. If successful, it returns a reference to the concrete type, otherwise it returns `None`.

## Code example:
```
use std::error::Error;

fn downcast_error(err: &dyn Error) -> Option<&dyn std::fmt::Debug> {
    err.downcast_ref::<&dyn std::fmt::Debug>()
}

fn main() {
    let err = std::io::Error::new(std::io::ErrorKind::Other, "oh no!");
    let downcast_err = downcast_error(&err);
    println!("downcast_err = {:?}", downcast_err);
}
```

### Output
```
downcast_err = None
```

Explanation:
- `use std::error::Error`: This imports the `Error` trait from the `std::error` module.
- `fn downcast_error(err: &dyn Error) -> Option<&dyn std::fmt::Debug>`: This function takes a reference to an `Error` trait object and attempts to downcast it to a concrete type.
- `err.downcast_ref::<&dyn std::fmt::Debug>()`: This is the method used to downcast the error. It takes a type parameter which is the type to which the error should be downcast.
- `let err = std::io::Error::new(std::io::ErrorKind::Other, "oh no!")`: This creates a new `std::io::Error` with the `ErrorKind::Other` and the message "oh no!".
- `let downcast_err = downcast_error(&err)`: This calls the `downcast_error` function with a reference to the `err` object.
- `println!("downcast_err = {:?}", downcast_err)`: This prints the result of the downcast attempt.

## Helpful links:
- [Rust Error Handling](https://doc.rust-lang.org/book/ch09-00-error-handling.html)
- [std::error::Error](https://doc.rust-lang.org/std/error/trait.Error.html#method.downcast_ref)