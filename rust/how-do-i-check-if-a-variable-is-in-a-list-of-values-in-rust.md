# How do I check if a variable is in a list of values in Rust?
// plain

You can check if a variable is in a list of values in Rust by using the `contains` method. This method takes a reference to the list and the value to search for as parameters.

## Example code

```rust
let list = [1, 2, 3, 4, 5];
let value = 3;

if list.contains(&value) {
    println!("The list contains the value!");
}
```

## Output example

```
The list contains the value!
```

## Code explanation

- `let list = [1, 2, 3, 4, 5];`: This line creates a list of values.
- `let value = 3;`: This line creates a variable to search for in the list.
- `if list.contains(&value)`: This line checks if the list contains the value.
- `println!("The list contains the value!");`: This line prints a message if the list contains the value.

## Helpful links
- [Rust Documentation - contains](https://doc.rust-lang.org/std/primitive.slice.html#method.contains)

group: rust-variables