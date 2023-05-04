# How to iterate an array in Rust
// plain

Iterating an array in Rust is a simple process. The `for` loop is the most common way to iterate an array. The following example code block shows how to iterate an array of integers:

```
let arr = [1, 2, 3, 4, 5];
for i in arr.iter() {
    println!("{}", i);
}
```

The output of the above code is:
```
1
2
3
4
5
```

The code consists of the following parts:
1. `let arr = [1, 2, 3, 4, 5];` - This declares an array of integers.
2. `for i in arr.iter()` - This is the `for` loop which iterates over the array.
3. `println!("{}", i);` - This prints the current element of the array.

For more information, please refer to the [Rust documentation](https://doc.rust-lang.org/book/ch03-05-control-flow.html#looping-through-a-collection-with-for).

group: rust-loops