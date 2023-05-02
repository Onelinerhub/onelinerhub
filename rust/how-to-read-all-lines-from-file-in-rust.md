# How to read all lines from file in Rust
// plain

Reading all lines from a file in Rust can be done using the `std::fs::read_to_string` function. This function takes a path to the file as an argument and returns a `Result<String, std::io::Error>` type. The `Result` type can be used to check for errors when reading the file. The following ## Code example shows how to read all lines from a file and print them out:

```rust
use std::fs;

fn main() {
    let file_contents = fs::read_to_string("my_file.txt").expect("Error reading file");
    println!("{}", file_contents);
}
```

In the ## Code example, the `fs::read_to_string` function is used to read the contents of the file into a `String` type. The `expect` method is used to check for errors when reading the file. If an error occurs, the `expect` method will panic and print out an error message. Finally, the contents of the file are printed out using the `println!` macro.

For more information on reading files in Rust, see the following links:

- [std::fs::read_to_string](https://doc.rust-lang.org/std/fs/fn.read_to_string.html)
- [std::io::Error](https://doc.rust-lang.org/std/io/struct.Error.html)
- [std::panic](https://doc.rust-lang.org/std/panic/index.html)

group: rust-files