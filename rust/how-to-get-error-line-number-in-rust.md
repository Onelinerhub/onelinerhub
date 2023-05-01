# How to get error line number in Rust
// plain

Rust provides a macro called `line!` which can be used to get the line number of the code.

Example code:
```
fn main() {
    println!("This is line number {}", line!());
}
```
### Output
```
This is line number 2
```

Explanation:
- `line!()`: This macro returns the line number of the code.
- `println!`: This macro is used to print the output to the console.

## Helpful links:
- https://doc.rust-lang.org/std/macro.line.html
- https://doc.rust-lang.org/std/macro.println.html