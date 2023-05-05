# How do you write a string to a file in Rust?
// plain

Writing a string to a file in Rust is a simple process. The following example code block shows how to do this:
```
use std::fs::File;
use std::io::prelude::*;

fn main() {
    let mut file = File::create("my_file.txt").expect("Failed to create file");
    let string = "Hello, world!";
    file.write_all(string.as_bytes()).expect("Failed to write to file");
}
```
## Code explanation


1. `use std::fs::File;`: This imports the `File` type from the `std::fs` module.
2. `use std::io::prelude::*;`: This imports the `write_all` method from the `std::io::prelude` module.
3. `let mut file = File::create("my_file.txt").expect("Failed to create file");`: This creates a new file called `my_file.txt` and assigns it to the `file` variable.
4. `let string = "Hello, world!";`: This creates a string variable called `string` and assigns it the value `"Hello, world!"`.
5. `file.write_all(string.as_bytes()).expect("Failed to write to file");`: This writes the contents of the `string` variable to the `file` variable.

The output of the example code is a file called `my_file.txt` containing the string `Hello, world!`.

## Helpful links

- [std::fs](https://doc.rust-lang.org/std/fs/)
- [std::io::prelude](https://doc.rust-lang.org/std/io/prelude/)