# How do you reverse a range in Rust?
// plain

Reversing a range in Rust is done using the `rev()` method. This method takes an iterator and returns an iterator that yields the same elements in reverse order.

## Example code

```
let mut range = 0..10;
let reversed_range = range.rev();

for x in reversed_range {
    println!("{}", x);
}
```

## Output example

```
9
8
7
6
5
4
3
2
1
0
```

## Code explanation

- `let mut range = 0..10;`: This creates a range from 0 to 10.
- `let reversed_range = range.rev();`: This creates a reversed range from 10 to 0 using the `rev()` method.
- `for x in reversed_range {`: This iterates over the reversed range.
- `println!("{}", x);`: This prints the current element of the reversed range.

## Helpful links
- [Rust Documentation - Iterator](https://doc.rust-lang.org/std/iter/trait.Iterator.html)
- [Rust Documentation - Range](https://doc.rust-lang.org/std/ops/struct.Range.html)