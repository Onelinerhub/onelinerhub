# How to get pointer to struct in Rust
// plain

In Rust, you can get a pointer to a struct by using the `&` operator. For example, if you have a struct called `MyStruct`, you can get a pointer to it by writing `&MyStruct`. This will return a pointer to the struct, which can then be used to access the fields of the struct. Additionally, you can use the `Box` type to create a pointer to a struct. This is done by writing `Box::new(MyStruct)`, which will return a pointer to the struct. Finally, you can use the `Rc` type to create a reference-counted pointer to a struct. This is done by writing `Rc::new(MyStruct)`, which will return a pointer to the struct.

Inline ## Code example:
```rust
let my_struct = MyStruct { ... };
let my_struct_ptr = &my_struct;
let my_struct_box = Box::new(my_struct);
let my_struct_rc = Rc::new(my_struct);
```

## Helpful links
- [Rust Reference - Pointers](https://doc.rust-lang.org/reference/pointers.html)
- [Rust Reference - Box](https://doc.rust-lang.org/reference/types/box.html)
- [Rust Reference - Rc](https://doc.rust-lang.org/reference/types/rc.html)

group: rust-pointers