# How to build rust program
// plain
The Rust language uses a build system called cargo to compile and build Rust programs. Cargo is a command-line tool that is used to compile and manage Rust projects, and it provides a number of helpful commands that make compiling and building Rust projects easier.

To build a Rust program, you first need to create a project directory and create a file named `main.rs` inside of it. This file should contain the code for your program.

For example, the following is a simple Rust program that prints "Hello, world!" to the console:

```rust
fn main() {
    println!("Hello, world!");
}
```

Once you have written your program, you can build it using cargo by running the following command in the project directory:

```
cargo build
```

This will compile your program and create an executable file in the `target/debug` directory. You can then run the executable file to execute your program.
