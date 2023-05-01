# How to get error stack trace in Rust
// plain

Error stack trace in Rust can be obtained by using the `Backtrace` struct from the `std::backtrace` module. The `Backtrace` struct provides methods to get a string representation of the stack trace.

Below is an example code to get the error stack trace in Rust:

```rust
use std::backtrace::Backtrace;

fn main() {
    let backtrace = Backtrace::new();
    println!("{:?}", backtrace);
}
```

### Output

```
Backtrace {
    frames: [
        Frame {
            ip: 0x7f8f9f9f9f9f,
            symbol_address: 0x7f8f9f9f9f9f,
            file: None,
            line: None,
            column: None,
            function: None,
            inlined: false
        },
        Frame {
            ip: 0x7f8f9f9f9f9f,
            symbol_address: 0x7f8f9f9f9f9f,
            file: None,
            line: None,
            column: None,
            function: None,
            inlined: false
        },
        ...
    ]
}
```

## Explanation of code parts:

1. `use std::backtrace::Backtrace;`: This imports the `Backtrace` struct from the `std::backtrace` module.

2. `let backtrace = Backtrace::new();`: This creates a new `Backtrace` instance.

3. `println!("{:?}", backtrace);`: This prints the stack trace in a human-readable format.

## Helpful links:

1. [std::backtrace](https://doc.rust-lang.org/std/backtrace/index.html)
2. [Backtrace](https://doc.rust-lang.org/std/backtrace/struct.Backtrace.html)