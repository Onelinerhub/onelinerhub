# How can I order strings in Rust?
// plain

Strings in Rust can be ordered using the `cmp` method. This method compares two strings and returns an `Ordering` enum which can be used to determine the ordering of the strings.

## Example code

```rust
let string1 = "Hello";
let string2 = "World";

let result = string1.cmp(&string2);

println!("{:?}", result);
```

## Output example

```
Less
```

The `cmp` method takes a reference to another string as an argument and returns an `Ordering` enum which can have one of three values: `Less`, `Equal`, or `Greater`. `Less` is returned when the first string is lexicographically less than the second string, `Equal` is returned when the strings are equal, and `Greater` is returned when the first string is lexicographically greater than the second string.

## Code explanation

- `let string1 = "Hello";`: This line declares a string variable called `string1` and assigns it the value `"Hello"`.
- `let string2 = "World";`: This line declares a string variable called `string2` and assigns it the value `"World"`.
- `let result = string1.cmp(&string2);`: This line calls the `cmp` method on `string1` and passes a reference to `string2` as an argument. The result of the `cmp` method is stored in the `result` variable.
- `println!("{:?}", result);`: This line prints the value of the `result` variable to the console.

## Helpful links
- [Rust Documentation - Strings](https://doc.rust-lang.org/std/string/struct.String.html)