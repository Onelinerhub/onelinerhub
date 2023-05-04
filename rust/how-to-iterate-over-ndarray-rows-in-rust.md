# How to iterate over ndarray rows in Rust
// plain

Iterating over ndarray rows in Rust can be done using the `.row_iter()` method. This method returns an iterator over the rows of the ndarray.

## Example code

```
let mut arr = ndarray::arr2(&[[1, 2], [3, 4]]);

for row in arr.row_iter() {
    println!("{:?}", row);
}
```

## Output example

```
[1 2]
[3 4]
```

## Code explanation

- `let mut arr = ndarray::arr2(&[[1, 2], [3, 4]]);`: creates a 2x2 ndarray with the given values
- `for row in arr.row_iter()`: iterates over the rows of the ndarray
- `println!("{:?}", row);`: prints the current row

## Helpful links
- [ndarray documentation](https://docs.rs/ndarray/0.13.0/ndarray/)

group: rust-loops