# How to get an element from a slice in Rust?
// plain

To get an element from a slice in Rust, you can use the `get` method. This method takes an index as an argument and returns an `Option<&T>` where `T` is the type of the elements in the slice.

```rust
let v = [10, 40, 30];
let third: Option<&i32> = v.get(2);
println!("The third element is {:?}", third);
```

## Output example

```
The third element is Some(30)
```

The code above does the following:

1. Declares a slice `v` with three elements of type `i32`.
2. Calls the `get` method on `v` with the index `2` as an argument.
3. Prints the result of the `get` method, which is an `Option<&i32>`.

## Helpful links

- [Slice documentation](https://doc.rust-lang.org/std/primitive.slice.html)
- [Option documentation](https://doc.rust-lang.org/std/option/enum.Option.html)

group: rust-slice