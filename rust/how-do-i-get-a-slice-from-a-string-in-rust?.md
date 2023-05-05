# How do I get a slice from a string in Rust?
// plain

You can get a slice from a string in Rust using the `slice` method. This method takes two parameters, the start index and the end index of the slice. The following example code will create a slice of the string `"Hello World"` from index 1 to index 5:

```rust
let s = "Hello World";
let slice = &s[1..5];
println!("{}", slice);
```

## Output example


```
ello
```

## Code explanation


- `let s = "Hello World";`: This creates a string variable `s` with the value `"Hello World"`.
- `let slice = &s[1..5];`: This creates a slice of the string `s` from index 1 to index 5 and assigns it to the variable `slice`.
- `println!("{}", slice);`: This prints the value of the variable `slice` to the console.

## Helpful links

- [String Slices in Rust](https://doc.rust-lang.org/book/ch04-03-slices.html)