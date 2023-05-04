# How to sort a struct in Rust
// plain

Sorting a struct in Rust can be done using the `sort_by` method on a vector of structs. This method takes a closure as an argument which defines the sorting criteria. The example code below sorts a vector of structs by the `name` field in ascending order.

```rust
struct Person {
    name: String,
    age: u8,
}

let mut people = vec![
    Person { name: "John".to_string(), age: 30 },
    Person { name: "Alice".to_string(), age: 20 },
    Person { name: "Bob".to_string(), age: 25 },
];

people.sort_by(|a, b| a.name.cmp(&b.name));

for person in people {
    println!("{} is {} years old", person.name, person.age);
}
```

## Output example

```
Alice is 20 years old
Bob is 25 years old
John is 30 years old
```

## Code explanation


1. `struct Person` - defines a struct with two fields, `name` and `age`, both of type `String` and `u8` respectively.
2. `let mut people = vec![...]` - creates a mutable vector of `Person` structs.
3. `people.sort_by(|a, b| a.name.cmp(&b.name))` - sorts the vector of `Person` structs by the `name` field in ascending order using the `sort_by` method. The closure passed to `sort_by` takes two arguments, `a` and `b`, and compares the `name` fields of each using the `cmp` method.
4. `for person in people { ... }` - iterates over the sorted vector of `Person` structs and prints out each person's name and age.

## Helpful links

- [Rust Book - Sorting](https://doc.rust-lang.org/book/ch13-02-iterators.html#sorting)
- [Rust Docs - sort_by](https://doc.rust-lang.org/std/vec/struct.Vec.html#method.sort_by)
- [Rust Docs - cmp](https://doc.rust-lang.org/std/primitive.str.html#method.cmp)

group: rust-struct