# An example of a range iterator in Rust?
// plain

An example of a range iterator in Rust is the `std::ops::Range` type. This type allows you to iterate over a range of values, such as all the numbers from 0 to 10.

```rust
for i in 0..10 {
    println!("{}", i);
}
```

## Output example

```
0
1
2
3
4
5
6
7
8
9
```

The code above creates a range from 0 to 10 and prints each number in the range. The `..` operator creates a range from the left-hand side to the right-hand side.

The `std::ops::Range` type is part of the Rust standard library and is used to create a range of values. It can be used to iterate over a range of values, such as numbers, characters, or other types.

## Helpful links
- [std::ops::Range](https://doc.rust-lang.org/std/ops/struct.Range.html)
- [Ranges - The Rust Programming Language](https://doc.rust-lang.org/book/ch03-02-data-types.html#ranges)