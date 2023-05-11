# How to pass a Rust HashMap as an argument?
// plain

Passing a Rust HashMap as an argument is done by using the `&` operator. This operator allows the HashMap to be passed by reference, meaning that the original HashMap is not copied.

## Example code

```
fn print_map(map: &HashMap<String, i32>) {
    for (key, value) in map {
        println!("{}: {}", key, value);
    }
}

fn main() {
    let mut map = HashMap::new();
    map.insert("one".to_string(), 1);
    map.insert("two".to_string(), 2);
    print_map(&map);
}
```

## Output example

```
one: 1
two: 2
```

## Code explanation

- `fn print_map(map: &HashMap<String, i32>)`: This is the function declaration, which takes a reference to a HashMap as an argument.
- `for (key, value) in map`: This loop iterates over the HashMap, allowing each key-value pair to be accessed.
- `println!("{}: {}", key, value);`: This prints the key-value pair to the console.
- `let mut map = HashMap::new();`: This creates a new, empty HashMap.
- `map.insert("one".to_string(), 1);`: This inserts a key-value pair into the HashMap.
- `print_map(&map);`: This passes the HashMap to the `print_map` function.

## Helpful links
- [Rust Documentation - HashMap](https://doc.rust-lang.org/std/collections/struct.HashMap.html)
- [Rust Documentation - Reference](https://doc.rust-lang.org/book/ch04-02-references-and-borrowing.html)

group: rust-hashmap

onelinerhub: [How to pass a Rust HashMap as an argument?](https://onelinerhub.com/rust/how-to-pass-a-rust-hashmap-as-an-argument)