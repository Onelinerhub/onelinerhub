# rust string comparison
// plain

String comparison in Rust is done using the `cmp` method. This method takes two strings as arguments and returns an `Ordering` enum, which can be either `Less`, `Equal`, or `Greater`.

## Example code

```rust
let string1 = "Hello";
let string2 = "World";

let comparison = string1.cmp(&string2);

println!("{:?}", comparison);
```

## Output example

```
Less
```

The `cmp` method compares two strings lexicographically, meaning it compares the characters in each string one by one until it finds a difference. In the example above, the first character of `string1` is `H`, which is less than the first character of `string2`, which is `W`. Therefore, the comparison returns `Less`.

## Code explanation

- `let string1 = "Hello";`: This line creates a string variable called `string1` and assigns it the value `Hello`.
- `let string2 = "World";`: This line creates a string variable called `string2` and assigns it the value `World`.
- `let comparison = string1.cmp(&string2);`: This line calls the `cmp` method on `string1` and passes `string2` as an argument. The `cmp` method returns an `Ordering` enum, which is stored in the `comparison` variable.
- `println!("{:?}", comparison);`: This line prints the value of the `comparison` variable to the console.

## Helpful links
- [Rust Documentation - Strings](https://doc.rust-lang.org/std/string/struct.String.html)