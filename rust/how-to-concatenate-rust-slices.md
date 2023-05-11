# How to concatenate Rust slices?
// plain

Rust slices can be concatenated using the `concat()` method. This method takes two slices and returns a new slice containing the elements of both slices.

## Example

```
let slice1 = [1, 2, 3];
let slice2 = [4, 5, 6];

let concatenated_slice = [slice1, slice2].concat();

println!("{:?}", concatenated_slice);
```
## Output example

```
[1, 2, 3, 4, 5, 6]
```

The code above consists of the following parts:

1. `let slice1 = [1, 2, 3];` - declaring a slice containing the elements `1`, `2` and `3`.
2. `let slice2 = [4, 5, 6];` - declaring a slice containing the elements `4`, `5` and `6`.
3. `let concatenated_slice = [slice1, slice2].concat();` - calling the `concat()` method on the slices `slice1` and `slice2` and assigning the result to the variable `concatenated_slice`.
4. `println!("{:?}", concatenated_slice);` - printing the contents of the `concatenated_slice` variable.

## Helpful links

- [Rust Documentation - Slices](https://doc.rust-lang.org/stable/std/primitive.slice.html)
- [Rust Documentation - Concatenation](https://doc.rust-lang.org/stable/std/primitive.slice.html#method.concat)

group: rust-slice