# How to write string to file in Rust
// plain

Writing a string to a file in Rust is a relatively straightforward process. First, you need to create a File object, which can be done using the `File::create` method. Then, you can use the `write_all` method to write the string to the file. Finally, you can use the `flush` method to ensure that the data is written to the file. An example of this process is shown below:
```rust
use std::fs::File;
use std::io::prelude::*;

fn main() {
    let mut file = File::create("my_file.txt").expect("Failed to create file");
    let data = "This is a string to write to the file";

    file.write_all(data.as_bytes()).expect("Failed to write to file");
    file.flush().expect("Failed to flush file");
}
```
In this example, we create a File object called `file` using the `File::create` method. We then use the `write_all` method to write the string `data` to the file. Finally, we use the `flush` method to ensure that the data is written to the file.

## Helpful links
- [File::create](https://doc.rust-lang.org/std/fs/struct.File.html#method.create)
- [write_all](https://doc.rust-lang.org/std/io/trait.Write.html#method.write_all)
- [flush](https://doc.rust-lang.org/std/io/trait.Write.html#method.flush)

group: rust-files