# How to loop for backward in Rust
// plain

Looping backward in Rust is done using the `rev()` method on an iterator. This method reverses the order of the iterator, allowing you to loop through it in reverse.

## Example code

```
let mut v = vec![1, 2, 3];

for i in v.iter().rev() {
    println!("{}", i);
}
```

## Output example

```
3
2
1
```

## Code explanation

- `let mut v = vec![1, 2, 3];`: creates a mutable vector with the values 1, 2, and 3.
- `for i in v.iter().rev()`: creates a loop that iterates over the vector in reverse order.
- `println!("{}", i);`: prints the current value of the loop.

## Helpful links
- [Rust Iterator Documentation](https://doc.rust-lang.org/std/iter/trait.Iterator.html)

group: rust-loops