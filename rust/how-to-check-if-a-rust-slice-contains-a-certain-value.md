# How to check if a Rust slice contains a certain value?
// plain

To check if a Rust slice contains a certain value, you can use the `contains()` method. This method takes a reference to the value you want to check for and returns a boolean value indicating whether the slice contains the value or not.

## Example code

```
let numbers = [1, 2, 3, 4, 5];
let contains_three = numbers.contains(&3);
```

## Output example

```
true
```

## Code explanation

- `let numbers = [1, 2, 3, 4, 5];`: This line creates a slice of numbers.
- `let contains_three = numbers.contains(&3);`: This line calls the `contains()` method on the `numbers` slice, passing in a reference to the value `3` as an argument.
- `true`: This is the output of the code, indicating that the `numbers` slice contains the value `3`.

## Helpful links
- [Rust Documentation - Slice](https://doc.rust-lang.org/std/primitive.slice.html)
- [Rust Documentation - contains()](https://doc.rust-lang.org/std/primitive.slice.html#method.contains)

group: rust-slice