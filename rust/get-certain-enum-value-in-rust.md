# Get certain enum value in Rust
// plain

In Rust, you can get a certain enum value by using the `.variant()` method. For example, if you have an enum called `Fruit` with variants `Apple`, `Orange`, and `Banana`, you can get the `Apple` variant by using `Fruit::Apple.variant()`. The output of this code would be `Apple`. The `.variant()` method is used to get the variant of an enum, which is the value associated with the enum. Additionally, you can use the `.is_variant()` method to check if a certain value is a variant of an enum. For example, `Fruit::Apple.is_variant()` would return `true`. ## Helpful links [Rust Enums](https://doc.rust-lang.org/book/ch06-01-defining-an-enum.html), [Enum Variants](https://doc.rust-lang.org/std/primitive.enum.html#variants), [Enum Methods](https://doc.rust-lang.org/std/primitive.enum.html#methods).

group: rust-enums