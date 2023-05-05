# How do I compare strings in Rust?
// plain

Strings in Rust can be compared using the `cmp()` method. This method returns an `Ordering` enum which can be used to determine if two strings are equal, one is greater than the other, or one is less than the other.

## Example

```
let string1 = "Hello";
let string2 = "World";

let comparison = string1.cmp(&string2);

println!("{:?}", comparison);
```

## Output example

```
Less
```

## Code explanation

- `let string1 = "Hello";`: This creates a string variable called `string1` and assigns it the value `"Hello"`.
- `let string2 = "World";`: This creates a string variable called `string2` and assigns it the value `"World"`.
- `let comparison = string1.cmp(&string2);`: This calls the `cmp()` method on `string1` and passes `string2` as an argument. This returns an `Ordering` enum which is assigned to the `comparison` variable.
- `println!("{:?}", comparison);`: This prints the value of the `comparison` variable to the console.

## Helpful links
- [Rust Documentation - Strings](https://doc.rust-lang.org/std/string/struct.String.html)