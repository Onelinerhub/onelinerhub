# Using linked lists in Rust
// plain

Using linked lists in Rust is a great way to store and manipulate data. Linked lists are a type of data structure that consists of a sequence of nodes, each containing a reference to the next node in the list. To create a linked list in Rust, you can use the standard library's LinkedList type. This type provides methods for adding, removing, and iterating over nodes in the list. To use the LinkedList type, you must first create a node structure that contains a reference to the next node in the list. Then, you can use the LinkedList methods to add, remove, and iterate over the nodes in the list.

```rust
use std::collections::LinkedList;

struct Node {
    data: i32,
    next: Option<Box<Node>>,
}

fn main() {
    let mut list = LinkedList::new();

    // Create a node
    let node1 = Node {
        data: 1,
        next: None,
    };

    // Add the node to the list
    list.push_back(Box::new(node1));

    // Iterate over the list
    for node in list.iter() {
        println!("{}", node.data);
    }
}
```

Output example:
```
1
```

## Explanation
 In this example, we create a Node structure that contains an integer data field and a reference to the next node in the list. We then create a LinkedList and add the node to it using the push_back() method. Finally, we iterate over the list using the iter() method, printing out the data field of each node.

## Helpful links
- [LinkedList documentation](https://doc.rust-lang.org/std/collections/struct.LinkedList.html)
- [Rust by Example - Linked Lists](https://doc.rust-lang.org/rust-by-example/std_misc/linked_list.html)
- [Rust Book - Linked Lists](https://doc.rust-lang.org/book/ch15-05-linked-lists.html)

group: linked-lists