# How to create a HashSet from a Range in Rust?
// plain

A HashSet can be created from a Range in Rust using the `collect` method. The `collect` method takes an iterator and collects its elements into a collection.

## Example code

```
let range = 0..10;
let set: HashSet<i32> = range.collect();
```

## Output example

```
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
```

## Code explanation

- `let range = 0..10;`: This creates a range from 0 to 10.
- `let set: HashSet<i32> = range.collect();`: This creates a HashSet from the range using the `collect` method.

## Helpful links
- [Rust Documentation - Iterator](https://doc.rust-lang.org/std/iter/trait.Iterator.html)
- [Rust Documentation - Collect](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.collect)
- [Rust Documentation - HashSet](https://doc.rust-lang.org/std/collections/struct.HashSet.html)

group: hashset

onelinerhub: [How to create a HashSet from a Range in Rust?](https://onelinerhub.com/rust/how-to-create-a-hashset-from-a-range-in-rust)