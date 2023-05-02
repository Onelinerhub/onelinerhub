# How to merge linked lists in Rust
// plain

To merge two linked lists in Rust, you can use the `append()` method. This method takes a reference to the list you want to append to and returns a mutable reference to the list. You can then iterate through the list you are appending and add each element to the end of the list you are appending to. For example:
```rust
let mut list1 = LinkedList::new();
let mut list2 = LinkedList::new();

// Add elements to list1 and list2

list1.append(&mut list2);
```
This will add all the elements of list2 to the end of list1. The output of this code will be a single linked list containing all the elements of both list1 and list2.

## Helpful links
- [LinkedList documentation](https://doc.rust-lang.org/std/collections/struct.LinkedList.html)
- [append() method documentation](https://doc.rust-lang.org/std/collections/struct.LinkedList.html#method.append)
- [Iterating over a LinkedList](https://doc.rust-lang.org/std/collections/struct.LinkedList.html#iterating-over-a-linkedlist)

group: linked-lists