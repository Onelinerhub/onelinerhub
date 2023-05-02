# How to append to file in Rust
// plain

Appending to a file in Rust is a relatively straightforward process. To do so, you need to open the file in write-only mode, seek to the end of the file, and then write the data you want to append. To open the file in write-only mode, you can use the `OpenOptions::append` method. To seek to the end of the file, you can use the `seek` method. Finally, to write the data, you can use the `write` method.

```rust
use std::fs::OpenOptions;
use std::io::{Seek, SeekFrom, Write};

fn main() {
    let mut file = OpenOptions::new()
        .write(true)
        .append(true)
        .open("my_file.txt")
        .unwrap();

    file.seek(SeekFrom::End(0)).unwrap();
    file.write(b"This is the data I want to append.").unwrap();
}
```

The above ## Code example opens the file `my_file.txt` in write-only mode and appends the data `This is the data I want to append.` to the end of the file.

## Helpful links
- [std::fs::OpenOptions](https://doc.rust-lang.org/std/fs/struct.OpenOptions.html)
- [std::io::Seek](https://doc.rust-lang.org/std/io/trait.Seek.html)
- [std::io::Write](https://doc.rust-lang.org/std/io/trait.Write.html)

group: rust-files