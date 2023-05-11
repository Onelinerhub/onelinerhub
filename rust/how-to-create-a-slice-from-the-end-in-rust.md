# How to create a slice from the end in Rust?
// plain

A slice in Rust is a data structure that allows you to reference a contiguous sequence of elements in a collection. To create a slice from the end of a collection, you can use the `.split_off()` method. This method takes an index as an argument and returns a tuple containing two slices. The first slice contains elements up to the index, and the second slice contains elements from the index to the end of the collection.

## Example code

```
let mut v = vec![1, 2, 3, 4, 5];
let (first, second) = v.split_off(3);

println!("First slice: {:?}", first);
println!("Second slice: {:?}", second);
```

## Output example

```
First slice: [1, 2, 3]
Second slice: [4, 5]
```

## Code explanation

- `let mut v = vec![1, 2, 3, 4, 5];`: creates a mutable vector with elements 1, 2, 3, 4, 5
- `let (first, second) = v.split_off(3);`: calls the `split_off()` method on the vector `v` with the index `3` as an argument, and assigns the returned tuple to the variables `first` and `second`
- `println!("First slice: {:?}", first);`: prints the contents of the `first` slice
- `println!("Second slice: {:?}", second);`: prints the contents of the `second` slice

## Helpful links
- [Rust Documentation - Vec::split_off()](https://doc.rust-lang.org/std/vec/struct.Vec.html#method.split_off)

group: rust-slice