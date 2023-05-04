# How to iterate lines in file in Rust
// plain

Iterating lines in a file in Rust is a simple task. The `std::fs::File` type provides a `lines` method which returns an iterator over the lines of the file. The following example code reads a file line by line and prints each line to the console:

```rust
use std::fs::File;
use std::io::{BufRead, BufReader};

fn main() {
    let file = File::open("my_file.txt").unwrap();
    let reader = BufReader::new(file);

    for line in reader.lines() {
        println!("{}", line.unwrap());
    }
}
```

## Output example

```
Line 1
Line 2
Line 3
```

## Code explanation


1. `use std::fs::File`: imports the `File` type from the `std::fs` module.
2. `let file = File::open("my_file.txt").unwrap()`: opens the file `my_file.txt` and stores the result in the `file` variable. The `unwrap` method is used to handle any errors that may occur.
3. `let reader = BufReader::new(file)`: creates a `BufReader` from the `file` variable.
4. `for line in reader.lines()`: iterates over the lines of the `reader` variable.
5. `println!("{}", line.unwrap())`: prints each line to the console. The `unwrap` method is used to handle any errors that may occur.

## Helpful links

- [std::fs::File](https://doc.rust-lang.org/std/fs/struct.File.html)
- [std::io::BufRead](https://doc.rust-lang.org/std/io/trait.BufRead.html)

group: rust-loops