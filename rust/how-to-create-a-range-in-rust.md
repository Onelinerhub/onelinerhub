# How to create a range in Rust?
// plain

Creating a range in Rust is a simple process. The `std::ops::Range` type is used to create a range of values. The `std::ops::Range` type is a struct that contains two fields, `start` and `end`.

## Example code

```
let range = std::ops::Range { start: 0, end: 10 };
```

## Output example

```
Range { start: 0, end: 10 }
```

The code above creates a range from 0 to 10. The `start` field is the starting value of the range, and the `end` field is the ending value of the range.

## Code explanation

- `let`: This is a keyword used to declare a variable.
- `range`: This is the name of the variable that will store the range.
- `std::ops::Range`: This is the type of the variable. It is used to create a range of values.
- `start`: This is the starting value of the range.
- `end`: This is the ending value of the range.

## Helpful links
- [Rust Documentation - std::ops::Range](https://doc.rust-lang.org/std/ops/struct.Range.html)