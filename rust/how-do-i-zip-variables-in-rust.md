# How do I zip variables in Rust?
// plain

Zipping variables in Rust is a way to combine two or more variables into a single data structure. This can be done using the `zip` method from the `Iterator` trait. The `zip` method takes two or more iterators and returns a new iterator of tuples, where each tuple contains one element from each of the input iterators.

## Example

```rust
let a = [1, 2, 3];
let b = [4, 5, 6];

let zipped = a.iter().zip(b.iter());

for (x, y) in zipped {
    println!("{} + {} = {}", x, y, x + y);
}
```
## Output example

```
1 + 4 = 5
2 + 5 = 7
3 + 6 = 9
```

## Code explanation

- `let a = [1, 2, 3];`: This creates an array of integers called `a`.
- `let b = [4, 5, 6];`: This creates an array of integers called `b`.
- `let zipped = a.iter().zip(b.iter());`: This creates a new iterator called `zipped` which combines the elements of `a` and `b` into tuples.
- `for (x, y) in zipped {`: This loop iterates over the tuples in `zipped`.
- `println!("{} + {} = {}", x, y, x + y);`: This prints out the sum of the elements in each tuple.

## Helpful links
- [Rust Documentation - Iterator Trait](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.zip)

group: rust-variables