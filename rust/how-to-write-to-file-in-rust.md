# How to write to file in Rust
// plain

Writing to a file in Rust is a straightforward process. First, you need to open a file in write-only mode using the `File::create` method. Then, you can write data to the file using the `write_all` method. Finally, you can close the file using the `close` method. The following ## Code example shows how to write a string to a file:
```rust
use std::fs::File;
use std::io::prelude::*;

fn main() {
    let mut file = File::create("my_file.txt").expect("Failed to create file");
    let data = "This is a string to write to the file";

    file.write_all(data.as_bytes()).expect("Failed to write to file");
}
```
In this example, we open a file called `my_file.txt` in write-only mode using the `File::create` method. Then, we write a string to the file using the `write_all` method. Finally, we close the file using the `close` method. After running this code, the file `my_file.txt` will contain the string `This is a string to write to the file`.

## Helpful links
- [File::create](https://doc.rust-lang.org/std/fs/struct.File.html#method.create)
- [write_all](https://doc.rust-lang.org/std/io/trait.Write.html#method.write_all)
- [close](https://doc.rust-lang.org/std/fs/struct.File.html#method.close)

group: rust-files