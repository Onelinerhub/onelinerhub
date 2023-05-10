# How do I copy a variable in Rust?
// plain

You can copy a variable in Rust by using the `clone()` method. This method will create a deep copy of the variable, meaning that the new variable will have the same value as the original, but will be stored in a different memory location.

## Example

```
let original = 5;
let copy = original.clone();
```

## Output example

```
No output
```

The code above creates a new variable `copy` with the same value as `original`.

## Code explanation

- `let original = 5;`: This line creates a variable `original` with the value `5`.
- `let copy = original.clone();`: This line creates a new variable `copy` with the same value as `original` by using the `clone()` method.

## Helpful links
- [Clone trait](https://doc.rust-lang.org/std/clone/trait.Clone.html)

group: rust-variables