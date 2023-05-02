# How to get pointer of struct in Rust
// plain

In Rust, you can get a pointer to a struct by using the `&` operator. For example, if you have a struct called `MyStruct`, you can get a pointer to it by writing `&MyStruct`. This will return a pointer to the struct, which can then be used to access the fields of the struct. Additionally, you can use the `&mut` operator to get a mutable pointer to the struct, which can be used to modify the fields of the struct. For example:
```rust
struct MyStruct {
    field1: i32,
    field2: i32,
}

fn main() {
    let my_struct = MyStruct { field1: 1, field2: 2 };
    let my_struct_ptr = &my_struct;
    let my_struct_mut_ptr = &mut my_struct;

    println!("field1: {}", my_struct_ptr.field1);
    println!("field2: {}", my_struct_mut_ptr.field2);

    my_struct_mut_ptr.field2 = 3;
    println!("field2: {}", my_struct_mut_ptr.field2);
}
```

Output example:
```
field1: 1
field2: 2
field2: 3
```

## Explanation

The `MyStruct` struct is declared with two fields, `field1` and `field2`. Then, a pointer to `MyStruct` is created using the `&` operator, and a mutable pointer is created using the `&mut` operator. The fields of the struct can then be accessed using the pointer, and the mutable pointer can be used to modify the fields of the struct.

## Helpful links
- [Rust Reference - Pointers](https://doc.rust-lang.org/reference/pointers.html)
- [Rust Reference - Structs](https://doc.rust-lang.org/reference/structs.html)
- [Rust Reference - Mutability](https://doc.rust-lang.org/reference/mutability.html)

group: rust-pointers