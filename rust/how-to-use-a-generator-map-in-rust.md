# How to use a generator map in Rust?
// plain

Using a generator map in Rust is a great way to create a map of values from an iterator. It is similar to the `map` method, but instead of returning a new iterator, it returns a `HashMap`.

## Example code

```rust
let v = vec![1, 2, 3];
let m: HashMap<_, _> = v.into_iter().map(|x| (x, x * x)).collect();
```

## Output example

```
{1: 1, 2: 4, 3: 9}
```

## Code explanation


- `let v = vec![1, 2, 3];`: This creates a vector with the values 1, 2, and 3.

- `let m: HashMap<_, _> =`: This creates a `HashMap` with the type of the keys and values left unspecified.

- `v.into_iter().map(|x| (x, x * x))`: This creates an iterator from the vector `v` and maps each value to a tuple of the value and its square.

- `collect()`: This collects the iterator into a `HashMap`.

## Helpful links

- [Rust Documentation - HashMap](https://doc.rust-lang.org/std/collections/struct.HashMap.html)
- [Rust Documentation - Iterator](https://doc.rust-lang.org/std/iter/trait.Iterator.html)

group: rust-generators