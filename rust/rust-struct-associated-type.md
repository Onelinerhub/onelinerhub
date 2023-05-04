# Rust struct associated type
// plain

A Rust struct associated type is a type parameter that is associated with a struct. It allows the struct to be generic over a type, meaning that the struct can be used with any type that meets the associated type's trait bounds. This is useful for creating data structures that can be used with different types of data.

## Example code

```rust
struct MyStruct<T> {
    data: T,
}

fn main() {
    let my_struct = MyStruct { data: 5 };
    println!("{}", my_struct.data);
}
```

## Output example

```
5
```

## Code explanation


- `struct MyStruct<T>`: This declares a struct called `MyStruct` that is generic over a type `T`.
- `data: T`: This declares a field called `data` that is of type `T`.
- `let my_struct = MyStruct { data: 5 }`: This creates an instance of `MyStruct` with the field `data` set to `5`.
- `println!("{}", my_struct.data)`: This prints the value of the `data` field of `my_struct`.

## Helpful links

- [Rust Struct Associated Type](https://doc.rust-lang.org/book/ch19-03-advanced-traits.html#associated-types)

group: rust-struct