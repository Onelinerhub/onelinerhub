# How to loop iterator in Rust
// plain

Looping over an iterator in Rust is done using the `for` loop. This loop will iterate over each element in the iterator and execute the code block within the loop.

```rust
let v = vec![1, 2, 3];

for i in v {
    println!("{}", i);
}
```

## Output example

```
1
2
3
```

The code above creates a vector `v` with three elements and then iterates over each element in the vector using the `for` loop. The code block within the loop prints out the value of the element.

## Code explanation

- `let v = vec![1, 2, 3];`: creates a vector `v` with three elements
- `for i in v {`: starts the `for` loop, which will iterate over each element in the vector `v`
- `println!("{}", i);`: prints out the value of the element
- `}`: ends the `for` loop

## Helpful links
- [Rust Documentation - Loops](https://doc.rust-lang.org/book/ch03-05-control-flow.html#loops)

group: rust-loops