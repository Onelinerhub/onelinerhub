# How to get an entry from a HashSet in Rust?
// plain

To get an entry from a HashSet in Rust, you can use the `get` method. This method takes a reference to the value you want to get and returns an `Option<&T>` where `T` is the type of the value stored in the HashSet.

## Example code

```rust
let mut set = HashSet::new();
set.insert("foo");

let entry = set.get(&"foo");
println!("{:?}", entry);
```

## Output example

```
Some("foo")
```

The code above creates a new HashSet and inserts a value of type `&str` into it. Then it uses the `get` method to get the entry with the value `"foo"`. The `get` method returns an `Option<&T>` where `T` is the type of the value stored in the HashSet. In this case, `T` is `&str` so the return type is `Option<&str>`. The output of the code is `Some("foo")` which indicates that the entry was found in the HashSet.

## Code explanation

- `let mut set = HashSet::new();`: creates a new HashSet
- `set.insert("foo");`: inserts a value of type `&str` into the HashSet
- `let entry = set.get(&"foo");`: uses the `get` method to get the entry with the value `"foo"`
- `println!("{:?}", entry);`: prints the result of the `get` method

## Helpful links
- [Rust HashSet documentation](https://doc.rust-lang.org/std/collections/struct.HashSet.html)

group: hashset

onelinerhub: [How to get an entry from a HashSet in Rust?](https://onelinerhub.com/rust/how-to-get-an-entry-from-a-hashset-in-rust)