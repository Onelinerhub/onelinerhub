# How to write buffer to file in Rust
// plain

Writing a buffer to a file in Rust is a simple process. To do this, you need to use the `std::fs::write` function. This function takes two parameters: a path to the file and a buffer containing the data to be written. The following ## Code example shows how to write a buffer to a file:
```rust
use std::fs;

let buffer = vec![1, 2, 3, 4, 5];
fs::write("my_file.txt", &buffer).expect("Unable to write file");
```
The example above will write the contents of the buffer to a file called `my_file.txt`. The `expect` function is used to handle any errors that may occur while writing the file.

The output of the ## Code example above will be a file called `my_file.txt` containing the data from the buffer.

The `std::fs::write` function takes two parameters: a path to the file and a buffer containing the data to be written. The path is a `std::path::Path` type, which is a type that represents a path to a file or directory. The buffer is a `&[u8]` type, which is a type that represents a slice of bytes.

The `expect` function is used to handle any errors that may occur while writing the file. If an error occurs, the `expect` function will panic and terminate the program.

## Helpful links
- [std::fs::write](https://doc.rust-lang.org/std/fs/fn.write.html)
- [std::path::Path](https://doc.rust-lang.org/std/path/struct.Path.html)
- [std::slice::SliceIndex](https://doc.rust-lang.org/std/slice/trait.SliceIndex.html)

group: rust-files