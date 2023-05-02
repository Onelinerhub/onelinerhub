# How to write line to file in Rust
// plain

Writing to a file in Rust is a relatively straightforward process. To do so, you must first open a file in write-only mode using the `File::create` method. Then, you can write data to the file using the `write_all` method. Finally, you must close the file using the `close` method. The following ## Code example shows how to write a line of text to a file:
```rust
use std::fs::File;
use std::io::prelude::*;

fn main() {
    let mut file = File::create("my_file.txt").expect("Failed to create file");
    let line = "This is a line of text written to a file.";
    file.write_all(line.as_bytes()).expect("Failed to write to file");
    file.close().expect("Failed to close file");
}
```
In this example, we first create a file called `my_file.txt` using the `File::create` method. Then, we write a line of text to the file using the `write_all` method. Finally, we close the file using the `close` method. After running this code, the file `my_file.txt` will contain the line of text that was written to it.

## Helpful links
- [File::create](https://doc.rust-lang.org/std/fs/struct.File.html#method.create)
- [write_all](https://doc.rust-lang.org/std/io/trait.Write.html#method.write_all)
- [close](https://doc.rust-lang.org/std/fs/struct.File.html#method.close)

group: rust-files