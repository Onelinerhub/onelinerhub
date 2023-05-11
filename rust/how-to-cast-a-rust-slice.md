# How to cast a Rust slice?
// plain

A Rust slice is a reference to a contiguous sequence of elements in a collection. It is a dynamically sized view into a contiguous memory block.

```
let arr = [1, 2, 3, 4, 5];
let slice = &arr[1..3];
println!("{:?}", slice);
```

## Output example

```
[2, 3]
```

To cast a Rust slice, you can use the `&` operator to create a reference to a portion of an array. The syntax is `&arr[start..end]`, where `start` is the index of the first element in the slice and `end` is the index of the element after the last element in the slice.

- `&` operator: creates a reference to a portion of an array
- `arr`: the array to create a slice from
- `start`: the index of the first element in the slice
- `end`: the index of the element after the last element in the slice

## Helpful links
- [Rust Slice Documentation](https://doc.rust-lang.org/std/primitive.slice.html)
- [Rust Slicing Tutorial](https://doc.rust-lang.org/book/ch04-03-slices.html)

group: rust-slice