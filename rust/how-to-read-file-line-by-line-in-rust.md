# How to read file line by line in rust
// plain

Reading a file line by line in Rust can be done using the `std::fs::File` type and the `BufReader` type from the `std::io::BufReader` module. To read a file line by line, first open the file in read-only mode using the `File::open` method. Then, create a `BufReader` from the file handle. Finally, use the `BufReader::lines` method to iterate over the lines of the file. The following ## Code example shows how to read a file line by line:
```rust
use std::fs::File;
use std::io::{BufReader, BufRead};

fn main() {
    let file = File::open("my_file.txt").expect("Unable to open file");
    let reader = BufReader::new(file);

    for line in reader.lines() {
        let line = line.expect("Unable to read line");
        println!("{}", line);
    }
}
```
In this example, the `File::open` method is used to open the file in read-only mode. Then, a `BufReader` is created from the file handle. Finally, the `BufReader::lines` method is used to iterate over the lines of the file. For each line, the `expect` method is used to unwrap the `Result` type and print the line.

## Helpful links
- [std::fs::File](https://doc.rust-lang.org/std/fs/struct.File.html)
- [std::io::BufReader](https://doc.rust-lang.org/std/io/struct.BufReader.html)
- [std::io::BufRead](https://doc.rust-lang.org/std/io/trait.BufRead.html)

group: rust-files