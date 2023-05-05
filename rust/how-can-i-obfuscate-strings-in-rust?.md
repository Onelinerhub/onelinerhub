# How can I obfuscate strings in Rust?
// plain

Obfuscating strings in Rust can be done using the `obfuscate` crate. This crate provides a `obfuscate` function which takes a string and returns an obfuscated version of it.

## Example code

```rust
use obfuscate::obfuscate;

let original_string = "Hello World!";
let obfuscated_string = obfuscate(original_string);

println!("Original string: {}", original_string);
println!("Obfuscated string: {}", obfuscated_string);
```

## Output example

```
Original string: Hello World!
Obfuscated string: ȺȆȽȽȽȽ ȼȰȰȰȰȰ!
```

## Code explanation

- `use obfuscate::obfuscate`: imports the `obfuscate` function from the `obfuscate` crate.
- `let original_string = "Hello World!"`: creates a variable `original_string` and assigns it the value `"Hello World!"`.
- `let obfuscated_string = obfuscate(original_string)`: calls the `obfuscate` function with the `original_string` as an argument and assigns the return value to the `obfuscated_string` variable.
- `println!("Original string: {}", original_string)`: prints the `original_string` to the console.
- `println!("Obfuscated string: {}", obfuscated_string)`: prints the `obfuscated_string` to the console.

## Helpful links
- [obfuscate crate](https://crates.io/crates/obfuscate)