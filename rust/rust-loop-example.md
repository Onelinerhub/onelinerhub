# Rust loop example
// plain

A `for` loop is a common type of loop in Rust. It allows you to iterate over a collection of items, such as an array or a vector.

```
let numbers = [1, 2, 3, 4, 5];

for number in numbers.iter() {
    println!("{}", number);
}
```

## Output example

```
1
2
3
4
5
```

The code above will loop through the `numbers` array and print out each element. The `iter()` method is used to get an iterator over the array. The `for` loop will then loop through each element in the iterator and print it out.

## Code explanation

- `let numbers = [1, 2, 3, 4, 5];`: This line declares an array of numbers.
- `for number in numbers.iter()`: This line starts the `for` loop. It will loop through each element in the `numbers` array.
- `println!("{}", number);`: This line prints out the current element in the loop.

## Helpful links
- [Rust Loops](https://doc.rust-lang.org/book/ch03-05-control-flow.html#loops)

group: rust-examples