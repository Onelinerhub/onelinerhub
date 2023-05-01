# How to merge iterators in Rust
// plain

Merging iterators in Rust can be done using the `chain()` method. This method takes two iterators and returns a new iterator that will iterate over both of them in sequence.

## Code example:
```
let iter1 = vec![1, 2, 3].into_iter();
let iter2 = vec![4, 5, 6].into_iter();

let merged_iter = iter1.chain(iter2);

for i in merged_iter {
    println!("{}", i);
}
```

### Output
```
1
2
3
4
5
6
```

Explanation:
- `let iter1 = vec![1, 2, 3].into_iter();`: This creates an iterator over the vector `[1, 2, 3]`.
- `let iter2 = vec![4, 5, 6].into_iter();`: This creates an iterator over the vector `[4, 5, 6]`.
- `let merged_iter = iter1.chain(iter2);`: This creates a new iterator that will iterate over both `iter1` and `iter2` in sequence.
- `for i in merged_iter {`: This loop will iterate over the `merged_iter` iterator.
- `println!("{}", i);`: This will print out the current value of `i` for each iteration of the loop.

## Helpful links:
- [Rust Iterator Documentation](https://doc.rust-lang.org/std/iter/)
- [Rust Chain Method Documentation](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.chain)