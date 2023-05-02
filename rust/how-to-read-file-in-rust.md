# How to read file in Rust
// plain

Reading a file in Rust is a straightforward process. The most common way to do this is to use the `std::fs::read_to_string` function, which takes a path to the file as an argument and returns a `Result<String, io::Error>`. This function will read the entire contents of the file into a `String` and return it. Alternatively, you can use the `std::fs::read` function, which takes a path to the file as an argument and returns a `Result<Vec<u8>, io::Error>`. This function will read the entire contents of the file into a `Vec<u8>` and return it.

```rust
use std::fs;

fn main() {
    let contents = fs::read_to_string("my_file.txt").expect("Error reading file");
    println!("File contents: {}", contents);
}
```

Output example:
```
File contents: This is the contents of my_file.txt
```

## Explanation

In this example, we use the `std::fs::read_to_string` function to read the contents of a file into a `String`. We pass the path to the file as an argument to the function, and it returns a `Result<String, io::Error>`. If the file is successfully read, the `Result` will contain the contents of the file as a `String`. If an error occurs, the `Result` will contain an `io::Error` describing the error.

We then use the `expect` method to unwrap the `Result` and get the contents of the file. If an error occurs, the `expect` method will panic and print the error message. Finally, we print the contents of the file using the `println!` macro.

## Helpful links
- [std::fs::read_to_string](https://doc.rust-lang.org/std/fs/fn.read_to_string.html)
- [std::fs::read](https://doc.rust-lang.org/std/fs/fn.read.html)
- [std::result](https://doc.rust-lang.org/std/result/enum.Result.html)

group: rust-files