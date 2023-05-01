# How to return error from main in Rust
// plain

The main function in Rust is the entry point of a program and it is required to return a value of type `std::process::ExitCode`. To return an error from main, you can use the `std::process::exit` function to return a non-zero value.

## Code example:

```
fn main() -> std::process::ExitCode {
    // Do something
    std::process::exit(1);
}
```

### Output

The program will exit with a non-zero exit code.

## Explanation of code parts:

1. `fn main() -> std::process::ExitCode`: This declares the main function and specifies that it returns a value of type `std::process::ExitCode`.
2. `std::process::exit(1)`: This calls the `std::process::exit` function with a parameter of `1`, which will cause the program to exit with a non-zero exit code.

## Helpful links:

1. [std::process::ExitCode](https://doc.rust-lang.org/std/process/enum.ExitCode.html)
2. [std::process::exit](https://doc.rust-lang.org/std/process/fn.exit.html)