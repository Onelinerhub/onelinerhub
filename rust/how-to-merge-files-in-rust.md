# How to merge files in Rust
// plain

Merging files in Rust can be done using the `std::fs::File` and `std::io::copy` functions. The following ## Code example shows how to merge two files into a third file:

```rust
use std::fs::File;
use std::io::{copy, Write};

fn main() {
    let mut file1 = File::open("file1.txt").expect("Unable to open file1");
    let mut file2 = File::open("file2.txt").expect("Unable to open file2");
    let mut file3 = File::create("file3.txt").expect("Unable to create file3");

    copy(&mut file1, &mut file3).expect("Unable to copy file1");
    copy(&mut file2, &mut file3).expect("Unable to copy file2");
}
```

This code will create a new file called `file3.txt` which will contain the contents of both `file1.txt` and `file2.txt`.

Explanation of code parts:

1. `use std::fs::File`: This imports the `File` type from the `std::fs` module, which is used to open files.
2. `use std::io::{copy, Write}`: This imports the `copy` and `Write` functions from the `std::io` module, which are used to copy data from one file to another and write data to a file, respectively.
3. `let mut file1 = File::open("file1.txt").expect("Unable to open file1")`: This opens the file `file1.txt` and stores a mutable reference to it in the `file1` variable. The `expect` method is used to handle any errors that may occur while opening the file.
4. `let mut file2 = File::open("file2.txt").expect("Unable to open file2")`: This opens the file `file2.txt` and stores a mutable reference to it in the `file2` variable. The `expect` method is used to handle any errors that may occur while opening the file.
5. `let mut file3 = File::create("file3.txt").expect("Unable to create file3")`: This creates a new file called `file3.txt` and stores a mutable reference to it in the `file3` variable. The `expect` method is used to handle any errors that may occur while creating the file.
6. `copy(&mut file1, &mut file3).expect("Unable to copy file1")`: This copies the contents of `file1` to `file3`. The `expect` method is used to handle any errors that may occur while copying the data.
7. `copy(&mut file2, &mut file3).expect("Unable to copy file2")`: This copies the contents of `file2` to `file3`. The `expect` method is used to handle any errors that may occur while copying the data.

## Helpful links:

1. [std::fs::File](https://doc.rust-lang.org/std/fs/struct.File.html)
2. [std::io::copy](https://doc.rust-lang.org/std/io/fn.copy.html)