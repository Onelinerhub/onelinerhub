# How to join two Rust slices?
// plain

Joining two Rust slices can be done using the `concat()` method. This method takes two slices and returns a new slice containing all the elements of both slices.

## Example

```
let slice1 = [1, 2, 3];
let slice2 = [4, 5, 6];

let joined_slice = [slice1, slice2].concat();

println!("{:?}", joined_slice);
```
## Output example

```
[1, 2, 3, 4, 5, 6]
```

The `concat()` method takes two slices and returns a new slice containing all the elements of both slices. The elements of the first slice are followed by the elements of the second slice.

## Code explanation

- `let slice1 = [1, 2, 3];`: This line creates a slice containing the elements `1`, `2`, and `3`.
- `let slice2 = [4, 5, 6];`: This line creates a slice containing the elements `4`, `5`, and `6`.
- `let joined_slice = [slice1, slice2].concat();`: This line calls the `concat()` method on the slices `slice1` and `slice2`, and stores the result in the variable `joined_slice`.
- `println!("{:?}", joined_slice);`: This line prints the contents of the `joined_slice` variable.

## Helpful links
- [Rust Documentation - Slices](https://doc.rust-lang.org/stable/std/primitive.slice.html)
- [Rust Documentation - Concat](https://doc.rust-lang.org/stable/std/primitive.slice.html#method.concat)

group: rust-slice