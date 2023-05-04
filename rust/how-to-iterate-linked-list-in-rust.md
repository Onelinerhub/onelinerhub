# How to iterate linked list in Rust
// plain

Iterating a linked list in Rust is done using a loop and the `.next()` method. The loop will continue until the `.next()` method returns `None`.

```rust
let mut current = list.head;
while let Some(node) = current {
    println!("{}", node.data);
    current = node.next;
}
```

## Code explanation


- `let mut current = list.head`: Declares a mutable variable `current` and assigns it to the head of the list.
- `while let Some(node) = current`: Begins a loop that will continue until `current` is `None`.
- `println!("{}", node.data)`: Prints the data of the current node.
- `current = node.next`: Assigns `current` to the next node in the list.

## Helpful links

- [Linked Lists in Rust](https://doc.rust-lang.org/book/ch15-05-linked-lists.html)
- [Rust Loops](https://doc.rust-lang.org/book/ch03-03-how-functions-work.html#loops)

group: rust-loops