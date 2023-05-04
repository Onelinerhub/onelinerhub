# How to iterate hashset in Rust
// plain

Iterating over a `HashSet` in Rust can be done using the `iter()` method. This method returns an iterator over the elements of the set.

## Example code

```
let mut set = HashSet::new();
set.insert("foo");
set.insert("bar");

for item in set.iter() {
    println!("{}", item);
}
```

## Output example

```
foo
bar
```

## Code explanation

- `let mut set = HashSet::new();`: creates a new empty `HashSet`
- `set.insert("foo");`: inserts the string `"foo"` into the `HashSet`
- `set.insert("bar");`: inserts the string `"bar"` into the `HashSet`
- `for item in set.iter() {`: starts an iterator over the elements of the `HashSet`
- `println!("{}", item);`: prints the current element of the `HashSet`
- `}`: ends the iterator

## Helpful links
- [HashSet documentation](https://doc.rust-lang.org/std/collections/struct.HashSet.html)
- [Iterator documentation](https://doc.rust-lang.org/std/iter/trait.Iterator.html)

group: rust-loops