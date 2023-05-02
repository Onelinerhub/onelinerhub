# Linked lists to string in Rust
// plain

Converting a linked list to a string in Rust is relatively straightforward. To do this, we can use the iter() method to iterate over the linked list and the collect() method to collect the elements into a string. The ## Code example below shows how to do this:
```rust
let mut list = LinkedList::new();
list.push_back("Hello");
list.push_back("World");

let list_string: String = list.iter().collect();
```
### Output example
The output of the above code would be a string containing the elements of the linked list, separated by commas:
```
"Hello, World"
```
### Explanation
The `iter()` method is used to iterate over the linked list, and the `collect()` method is used to collect the elements into a string. The `collect()` method takes an argument which specifies the type of the output, in this case a `String`.

### Relevant links
- [LinkedList documentation](https://doc.rust-lang.org/std/collections/struct.LinkedList.html)
- [iter() method documentation](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.iter)
- [collect() method documentation](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.collect)

group: linked-lists