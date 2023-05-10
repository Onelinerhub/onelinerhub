# How do I write a variable to a file in Rust?
// plain

Writing a variable to a file in Rust is a simple process. To do this, you will need to use the `std::fs::write` function. This function takes two parameters, the first being the path to the file you want to write to, and the second being the data you want to write.

```rust
use std::fs::write;

let data = "Hello, world!";
write("my_file.txt", data).expect("Unable to write file");
```

The code above will write the string `Hello, world!` to a file called `my_file.txt`.

The code consists of the following parts:

1. `use std::fs::write;` - This imports the `write` function from the `std::fs` module.
2. `let data = "Hello, world!";` - This creates a variable called `data` and assigns it the value `Hello, world!`.
3. `write("my_file.txt", data).expect("Unable to write file");` - This calls the `write` function, passing it the path to the file we want to write to (`my_file.txt`) and the data we want to write (`data`).

## Helpful links

- [std::fs::write](https://doc.rust-lang.org/std/fs/fn.write.html)

group: rust-variables