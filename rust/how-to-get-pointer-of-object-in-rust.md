# How to get pointer of object in Rust
// plain

In Rust, you can get a pointer to an object by using the `&` operator. For example, if you have an object `my_object` of type `MyObject`, you can get a pointer to it by writing `&my_object`. This will return a pointer of type `&MyObject`. You can then use this pointer to access the object's fields and methods. Additionally, you can use the `Box` type to create a pointer to an object on the heap. For example, `let my_box = Box::new(my_object);` will create a pointer to `my_object` on the heap.

```rust
struct MyObject {
    field1: i32,
    field2: i32,
}

fn main() {
    let my_object = MyObject { field1: 1, field2: 2 };
    let my_pointer = &my_object;
    let my_box = Box::new(my_object);

    println!("Pointer to my_object: {:?}", my_pointer);
    println!("Box containing my_object: {:?}", my_box);
}
```

### Output example
```
Pointer to my_object: &MyObject { field1: 1, field2: 2 }
Box containing my_object: Box { 0: MyObject { field1: 1, field2: 2 } }
```

### Explanation
The `&` operator is used to get a pointer to an object. In this example, `my_pointer` is a pointer to `my_object`. The `Box` type is used to create a pointer to an object on the heap. In this example, `my_box` is a pointer to `my_object` on the heap.

### Relevant links
- [Rust Reference - Pointers](https://doc.rust-lang.org/reference/pointers.html)
- [Rust Reference - Box](https://doc.rust-lang.org/std/boxed/struct.Box.html)
- [Rust Reference - Operators](https://doc.rust-lang.org/reference/operators.html)

group: rust-pointers