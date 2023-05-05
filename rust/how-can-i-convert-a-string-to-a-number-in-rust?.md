# How can I convert a string to a number in Rust?
// plain

You can convert a string to a number in Rust using the `parse` method. This method is available on all types that implement the `FromStr` trait. For example, to convert a string to an integer:

```rust
let s = "42";
let n: i32 = s.parse().unwrap();
println!("{}", n);
```

## Output example

```
42
```

The code above consists of the following parts:

1. `let s = "42";` - This declares a variable `s` of type `&str` and assigns it the value `"42"`.
2. `let n: i32 = s.parse().unwrap();` - This declares a variable `n` of type `i32` and assigns it the result of parsing the string `s` into an integer. The `unwrap` method is used to handle any errors that may occur during the parsing process.
3. `println!("{}", n);` - This prints the value of `n` to the console.

For more information, see the [Rust documentation](https://doc.rust-lang.org/std/primitive.str.html#method.parse).