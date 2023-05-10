# How do I pass variable arguments in Rust?
// plain

Variable arguments in Rust can be passed using the `std::env::args()` function. This function returns an iterator of the command line arguments passed to the program.

## Example code

```
fn main() {
    let args: Vec<String> = std::env::args().collect();
    println!("{:?}", args);
}
```

## Output example

```
["./my_program", "arg1", "arg2", "arg3"]
```

## Code explanation

- `std::env::args()`: This function returns an iterator of the command line arguments passed to the program.
- `let args: Vec<String> = std::env::args().collect();`: This line collects the arguments into a vector of strings.
- `println!("{:?}", args);`: This line prints the vector of strings.

## Helpful links
- [std::env::args()](https://doc.rust-lang.org/std/env/fn.args.html)

group: rust-variables