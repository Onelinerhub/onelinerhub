# How do I share a variable between structs in Rust?
// plain

You can share a variable between structs in Rust by using a reference. A reference is a type of pointer that allows you to refer to a value without taking ownership of it. To create a reference, use the `&` operator.

```rust
struct Foo {
    x: i32,
}

struct Bar {
    y: &Foo,
}

fn main() {
    let foo = Foo { x: 10 };
    let bar = Bar { y: &foo };
    println!("{}", bar.y.x);
}
```

## Output example

```
10
```

## Code explanation


1. `struct Foo { x: i32, }` - This creates a struct called `Foo` with a field `x` of type `i32`.
2. `struct Bar { y: &Foo, }` - This creates a struct called `Bar` with a field `y` of type `&Foo`, which is a reference to a `Foo` struct.
3. `let foo = Foo { x: 10 };` - This creates a `Foo` struct with the value of `x` set to `10`.
4. `let bar = Bar { y: &foo };` - This creates a `Bar` struct with the value of `y` set to a reference of the `foo` struct.
5. `println!("{}", bar.y.x);` - This prints the value of `x` from the `foo` struct, which is `10`.

## Helpful links

- [Rust Reference](https://doc.rust-lang.org/reference/index.html)
- [Rust Ownership](https://doc.rust-lang.org/book/ch04-01-what-is-ownership.html)

group: rust-variables