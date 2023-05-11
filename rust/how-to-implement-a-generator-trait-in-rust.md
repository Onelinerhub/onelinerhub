# How to implement a generator trait in Rust?
// plain

Generator traits are a powerful tool for creating iterators in Rust. They allow for the creation of custom iterators that can be used to iterate over collections of data.

## Example code

```rust
use std::iter::Generator;

struct MyGenerator {
    // ...
}

impl Generator for MyGenerator {
    type Yield = i32;
    type Return = ();

    fn resume(&mut self) -> GeneratorState<Self::Yield, Self::Return> {
        // ...
    }
}
```

The code above creates a custom generator trait called `MyGenerator`. It implements the `Generator` trait from the `std::iter` module. The `Yield` and `Return` types are specified as `i32` and `()` respectively. The `resume` method is then implemented, which is responsible for yielding values from the generator.

## Code explanation


- `use std::iter::Generator`: This imports the `Generator` trait from the `std::iter` module.
- `struct MyGenerator`: This creates a custom generator struct.
- `impl Generator for MyGenerator`: This implements the `Generator` trait for the `MyGenerator` struct.
- `type Yield = i32` and `type Return = ()`: These specify the types of values that the generator will yield and return respectively.
- `fn resume(&mut self) -> GeneratorState<Self::Yield, Self::Return>`: This is the implementation of the `resume` method, which is responsible for yielding values from the generator.

## Helpful links

- [Generator Trait](https://doc.rust-lang.org/std/iter/trait.Generator.html)
- [Generator State](https://doc.rust-lang.org/std/iter/enum.GeneratorState.html)

group: rust-generators