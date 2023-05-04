# How to convert struct to protobuf in Rust
// plain

Converting a struct to protobuf in Rust is done using the [`prost`](https://github.com/danburkert/prost) crate.

To convert a struct to protobuf, the struct must first be annotated with `#[derive(Message)]` and the fields must be annotated with `#[prost(...)]`.

## Example code

```rust
#[derive(Message)]
struct MyStruct {
    #[prost(int32, tag = "1")]
    my_field: i32,
}
```

The `#[derive(Message)]` annotation tells the compiler to generate code to serialize and deserialize the struct into protobuf. The `#[prost(...)]` annotation tells the compiler how to serialize and deserialize the field.

The generated code can then be used to convert the struct to protobuf:

```rust
let my_struct = MyStruct { my_field: 42 };
let mut buf = Vec::new();
my_struct.encode(&mut buf).unwrap();
```

The `encode` method serializes the struct into protobuf and writes it to the `buf` vector.

group: rust-struct