# rust string compare
// plain

Rust strings can be compared using the `cmp()` method. This method takes two strings as parameters and returns an `Ordering` enum which can be `Less`, `Equal` or `Greater`.

## Example

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

The `cmp()` method compares the two strings lexicographically and returns the result as an `Ordering` enum. The `Ordering` enum can be `Less` if the first string is lexicographically less than the second string, `Equal` if the two strings are equal, and `Greater` if the first string is lexicographically greater than the second string.

## Helpful links

- [Rust Documentation - Strings](https://doc.rust-lang.org/std/string/struct.String.html)
- [Rust Documentation - Ordering](https://doc.rust-lang.org/std/cmp/enum.Ordering.html)