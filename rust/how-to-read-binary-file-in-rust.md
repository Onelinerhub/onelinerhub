# How to read binary file in Rust
// plain

Reading a binary file in Rust is relatively straightforward. First, you need to open the file using the `std::fs::File::open` method. Then, you can read the contents of the file using the `std::io::Read` trait. Finally, you can convert the bytes into a usable format, such as a `Vec<u8>` or a `String`. The following ## Code example shows how to read a binary file and convert it into a `Vec<u8>`:

```rust
use std::fs::File;
use std::io::Read;

fn main() {
    let mut file = File::open("my_file.bin").expect("Failed to open file");
    let mut contents = Vec::new();
    file.read_to_end(&mut contents).expect("Failed to read file");
}
```

In this example, we open the file using the `File::open` method, then read the contents of the file into a `Vec<u8>` using the `read_to_end` method. The `expect` method is used to handle any errors that may occur while opening or reading the file.

If you need to convert the bytes into a `String`, you can use the `String::from_utf8` method. The following example shows how to convert the bytes into a `String`:

```rust
use std::fs::File;
use std::io::Read;

fn main() {
    let mut file = File::open("my_file.bin").expect("Failed to open file");
    let mut contents = Vec::new();
    file.read_to_end(&mut contents).expect("Failed to read file");
    let contents_string = String::from_utf8(contents).expect("Failed to convert bytes to string");
}
```

In this example, we use the `String::from_utf8` method to convert the bytes into a `String`. The `expect` method is used to handle any errors that may occur while converting the bytes.

## Helpful links

- [std::fs::File](https://doc.rust-lang.org/std/fs/struct.File.html)
- [std::io::Read](https://doc.rust-lang.org/std/io/trait.Read.html)
- [String::from_utf8](https://doc.rust-lang.org/std/string/struct.String.html#method.from_utf8)

group: rust-files