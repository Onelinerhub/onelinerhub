# How to write struct to file in Rust
// plain

Writing a struct to a file in Rust is relatively straightforward. First, you need to create a File object, which can be done using the `File::create` method. Then, you need to serialize the struct into a byte array, which can be done using the `bincode` crate. Finally, you can write the byte array to the file using the `write_all` method. An example of this process is shown below:
```rust
use std::fs::File;
use bincode::{serialize, deserialize};

#[derive(Serialize, Deserialize)]
struct MyStruct {
    field1: i32,
    field2: String,
}

fn main() {
    let my_struct = MyStruct {
        field1: 5,
        field2: String::from("Hello World!"),
    };

    let serialized = serialize(&my_struct).unwrap();

    let mut file = File::create("my_struct.bin").unwrap();
    file.write_all(&serialized).unwrap();
}
```
The output of this code is a binary file called `my_struct.bin` which contains the serialized version of the struct.

## Helpful links
- [File::create](https://doc.rust-lang.org/std/fs/struct.File.html#method.create)
- [bincode](https://docs.rs/bincode/1.2.1/bincode/)
- [write_all](https://doc.rust-lang.org/std/io/trait.Write.html#method.write_all)

group: rust-files