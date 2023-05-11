# How to delete an entry from a Rust HashMap?
// plain

To delete an entry from a Rust HashMap, the `remove` method can be used. The `remove` method takes a key as an argument and returns the value associated with the key if it exists.

## Example code

```
use std::collections::HashMap;

let mut scores = HashMap::new();

scores.insert(String::from("Blue"), 10);
scores.insert(String::from("Yellow"), 50);

let blue_score = scores.remove("Blue");

println!("Blue score: {:?}", blue_score);
```

## Output example

```
Blue score: Some(10)
```

## Code explanation


1. `use std::collections::HashMap;`: This imports the `HashMap` type from the `std::collections` module.

2. `let mut scores = HashMap::new();`: This creates a new empty `HashMap` called `scores`.

3. `scores.insert(String::from("Blue"), 10);`: This inserts a key-value pair into the `HashMap`, with the key being a `String` with the value `"Blue"` and the value being an `i32` with the value `10`.

4. `let blue_score = scores.remove("Blue");`: This removes the key-value pair with the key `"Blue"` from the `HashMap` and stores the associated value in the variable `blue_score`.

5. `println!("Blue score: {:?}", blue_score);`: This prints the value stored in `blue_score` to the console.

## Helpful links

- [Rust HashMap Documentation](https://doc.rust-lang.org/std/collections/struct.HashMap.html)

group: rust-hashmap

onelinerhub: [How to delete an entry from a Rust HashMap?](https://onelinerhub.com/rust/how-to-delete-an-entry-from-a-rust-hashmap)