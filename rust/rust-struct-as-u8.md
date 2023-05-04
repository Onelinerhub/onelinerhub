# Rust struct as u8
// plain

A Rust `struct` can be converted to a `u8` (unsigned 8-bit integer) using the `From` trait. This trait allows a type to be converted into another type.

## Example code

```rust
struct MyStruct {
    value: u8
}

let my_struct = MyStruct { value: 5 };
let my_u8: u8 = my_struct.into();

assert_eq!(my_u8, 5);
```

## Output example

```
assertion successful
```

The code above creates a `struct` called `MyStruct` with a single field `value` of type `u8`. The `into()` method is then used to convert the `struct` into a `u8`. The `assert_eq!` macro is then used to check that the value of the `u8` is equal to the value of the `struct`.

## Code explanation


1. `struct MyStruct { value: u8 }` - This creates a `struct` called `MyStruct` with a single field `value` of type `u8`.
2. `let my_struct = MyStruct { value: 5 }` - This creates an instance of `MyStruct` with the value of `value` set to `5`.
3. `let my_u8: u8 = my_struct.into()` - This uses the `into()` method to convert the `struct` into a `u8`.
4. `assert_eq!(my_u8, 5)` - This uses the `assert_eq!` macro to check that the value of the `u8` is equal to the value of the `struct`.

## Helpful links

- [Rust `struct` documentation](https://doc.rust-lang.org/book/ch05-01-defining-structs.html)
- [Rust `From` trait documentation](https://doc.rust-lang.org/std/convert/trait.From.html)
- [Rust `assert_eq!` macro documentation](https://doc.rust-lang.org/std/macro.assert_eq.html)

group: rust-struct