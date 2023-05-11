# How to get the last n elements from a slice in Rust?
// plain

To get the last n elements from a slice in Rust, you can use the `.split_last()` method. This method takes a slice and returns a tuple of two slices, the first being the elements before the last n elements, and the second being the last n elements.

## Example code

```
let v = [1, 2, 3, 4, 5];
let (first, last) = v.split_last().unwrap();
println!("First: {:?}, Last: {:?}", first, last);
```

## Output example

```
First: [1, 2, 3], Last: [4, 5]
```

## Code explanation

- `let v = [1, 2, 3, 4, 5];`: This creates a slice of 5 elements.
- `let (first, last) = v.split_last().unwrap();`: This uses the `.split_last()` method to split the slice into two slices, the first being the elements before the last n elements, and the second being the last n elements.
- `println!("First: {:?}, Last: {:?}", first, last);`: This prints the two slices.

## Helpful links
- [Rust Documentation - Slice](https://doc.rust-lang.org/std/primitive.slice.html)
- [Rust Documentation - split_last()](https://doc.rust-lang.org/std/primitive.slice.html#method.split_last)

group: rust-slice