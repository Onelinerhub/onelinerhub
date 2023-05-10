# How to zip maps in Rust?
// plain

Zipping maps in Rust is a simple process. To do so, you can use the `zip` method from the `Iterator` trait. This method takes two iterators and returns a new iterator of pairs, where the first element of each pair is taken from the first iterator, and the second element is taken from the second iterator.

```rust
let map1 = [1, 2, 3];
let map2 = [4, 5, 6];

let zipped_map = map1.iter().zip(map2.iter());

for pair in zipped_map {
    println!("{:?}", pair);
}
```

## Output example

```
(1, 4)
(2, 5)
(3, 6)
```

The code above creates two maps, `map1` and `map2`, and then uses the `zip` method to create a new iterator of pairs from the two maps. Finally, the code iterates over the pairs and prints them out.

Parts of the code:
- `let map1 = [1, 2, 3];`: creates a map with the values 1, 2, and 3.
- `let map2 = [4, 5, 6];`: creates a map with the values 4, 5, and 6.
- `let zipped_map = map1.iter().zip(map2.iter());`: creates a new iterator of pairs from the two maps.
- `for pair in zipped_map {`: iterates over the pairs.
- `println!("{:?}", pair);`: prints out the pairs.

## Helpful links
- [Iterator Trait](https://doc.rust-lang.org/std/iter/trait.Iterator.html)

group: rust-zip