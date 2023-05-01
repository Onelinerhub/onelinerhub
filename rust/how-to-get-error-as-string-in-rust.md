# How to get error as string in Rust
// plain

In Rust, you can get the error as a string using the `to_string()` method. This method is available on the `std::error::Error` trait, which is implemented by all types that implement the `std::error::Error` trait.

## Code example:
```
use std::error::Error;

fn main() {
    let err: Box<dyn Error> = Box::new(std::io::Error::new(std::io::ErrorKind::Other, "oh no!"));
    let err_string = err.to_string();
    println!("Error as string: {}", err_string);
}
```

### Output
```
Error as string: Other: oh no!
```

## Explanation of code parts:
1. `use std::error::Error;`: This imports the `Error` trait from the `std::error` module.
2. `let err: Box<dyn Error> = Box::new(std::io::Error::new(std::io::ErrorKind::Other, "oh no!"));`: This creates a `Box` containing an `Error` instance with the `ErrorKind` of `Other` and the message `"oh no!"`.
3. `let err_string = err.to_string();`: This calls the `to_string()` method on the `Error` instance, which returns the error as a string.
4. `println!("Error as string: {}", err_string);`: This prints the error string to the console.

## Helpful links:
1. [Rust Documentation - Error](https://doc.rust-lang.org/std/error/trait.Error.html)
2. [Rust Documentation - ErrorKind](https://doc.rust-lang.org/std/io/enum.ErrorKind.html)