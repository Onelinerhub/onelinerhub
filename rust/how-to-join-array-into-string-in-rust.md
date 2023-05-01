# How to join array into string in Rust
// plain

Joining an array into a string in Rust can be done using the `join` method. This method takes a separator as an argument and returns a String.

## Code example:

```
let arr = ["Hello", "World"];
let joined_string = arr.join(" ");
println!("{}", joined_string);
```

### Output

`Hello World`

Explanation:

1. The `let arr = ["Hello", "World"];` line creates an array of strings.
2. The `let joined_string = arr.join(" ");` line calls the `join` method on the array, passing in a space as the separator.
3. The `println!("{}", joined_string);` line prints the joined string to the console.

## Helpful links:

1. [Rust Documentation - Strings](https://doc.rust-lang.org/std/string/index.html)
2. [Rust Documentation - Arrays](https://doc.rust-lang.org/std/primitive.array.html)