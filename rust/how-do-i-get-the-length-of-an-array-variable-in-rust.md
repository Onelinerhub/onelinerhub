# How do I get the length of an array variable in Rust?
// plain

The length of an array variable in Rust can be obtained using the `len()` method. This method returns the number of elements in the array.

## Example code

```
let arr = [1, 2, 3, 4, 5];
let arr_length = arr.len();
```

## Output example

```
5
```

## Code explanation

- `let arr = [1, 2, 3, 4, 5];`: This line declares an array variable `arr` with 5 elements.
- `let arr_length = arr.len();`: This line calls the `len()` method on the `arr` array variable and assigns the result to the `arr_length` variable.
- `arr.len()`: This is the `len()` method which returns the number of elements in the array.

## Helpful links
- [Rust Documentation - Arrays](https://doc.rust-lang.org/std/primitive.array.html)

group: rust-variables