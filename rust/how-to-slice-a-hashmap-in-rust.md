# How to slice a hashmap in Rust?
// plain

Slicing a hashmap in Rust is done using the `.iter()` method. This method returns an iterator over the key-value pairs of the hashmap. The iterator can then be used to access the elements of the hashmap.

## Example code

```
let mut my_hashmap = HashMap::new();
my_hashmap.insert("a", 1);
my_hashmap.insert("b", 2);
my_hashmap.insert("c", 3);

for (key, value) in my_hashmap.iter() {
    println!("{}: {}", key, value);
}
```

## Output example

```
a: 1
b: 2
c: 3
```

## Code explanation

- `let mut my_hashmap = HashMap::new();`: This line creates a new empty hashmap.
- `my_hashmap.insert("a", 1);`: This line inserts a key-value pair into the hashmap.
- `for (key, value) in my_hashmap.iter() {`: This line creates an iterator over the key-value pairs of the hashmap.
- `println!("{}: {}", key, value);`: This line prints out the key-value pairs of the hashmap.

## Helpful links
- [Rust HashMap Documentation](https://doc.rust-lang.org/std/collections/struct.HashMap.html)

group: rust-slice