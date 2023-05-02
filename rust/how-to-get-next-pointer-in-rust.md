# How to get next pointer in Rust
// plain

In Rust, the next pointer can be accessed using the `.next()` method. This method returns an Option type, which can be used to check if the pointer is valid or not. For example, the following code snippet shows how to access the next pointer of a linked list node:
```rust
let mut node = list.head;
while let Some(next_node) = node.next() {
    node = next_node;
}
```
In the code snippet, the `.next()` method is used to get the next pointer of the current node. The `while let` loop is used to iterate through the linked list until the `next_node` is `None`.

## Helpful links
- [Rust Documentation - Option](https://doc.rust-lang.org/std/option/enum.Option.html)
- [Rust Documentation - Linked List](https://doc.rust-lang.org/std/collections/struct.LinkedList.html)
- [Rust by Example - Linked List](https://doc.rust-lang.org/rust-by-example/std/linked_list.html)

group: rust-pointers