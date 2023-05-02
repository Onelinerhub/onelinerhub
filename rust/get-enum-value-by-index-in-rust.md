# Get enum value by index in Rust
// plain

In Rust, you can get the enum value by index using the `.nth()` method. This method takes an index as an argument and returns the enum value at that index. For example, if you have an enum called `Fruit` with values `Apple`, `Banana`, and `Orange`, you can get the value at index 1 using `Fruit::nth(1)`. This will return `Banana`. You can also use the `.iter()` method to iterate over all the enum values. For example, `Fruit::iter()` will return an iterator over all the enum values.
```rust
enum Fruit {
    Apple,
    Banana,
    Orange,
}

let fruit = Fruit::nth(1);
println!("{:?}", fruit);
```

### Output example
```
Banana
```

### Explanation
The `Fruit` enum is declared with three values: `Apple`, `Banana`, and `Orange`. The `Fruit::nth(1)` method is used to get the enum value at index 1, which is `Banana`. The `println!` macro is used to print the value of `fruit`, which is `Banana`.

### Relevant links
[Rust Enums](https://doc.rust-lang.org/book/ch06-01-defining-an-enum.html)

[Rust Iterators](https://doc.rust-lang.org/book/ch13-01-what-is-an-iterator.html)

[Rust println! Macro](https://doc.rust-lang.org/std/macro.println.html)

group: rust-enums