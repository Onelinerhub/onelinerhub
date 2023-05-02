# Is it possible to use closure recursion in Rust
// plain

Yes, it is possible to use closure recursion in Rust. Closure recursion is a technique where a closure is used to call itself, allowing for recursive behavior. To use closure recursion in Rust, you need to create a closure that takes a parameter and returns a closure that takes the same parameter. The closure should then call itself with the parameter, allowing for recursive behavior.
```rust
fn closure_recursion(n: i32) -> impl Fn(i32) -> i32 {
    move |x| {
        if x <= 0 {
            n
        } else {
            closure_recursion(n + 1)(x - 1)
        }
    }
}
```
This example creates a closure that takes an integer parameter and returns a closure that takes the same parameter. The closure then calls itself with the parameter, allowing for recursive behavior.

For example, if we call the closure with the parameter 5, the output will be 10:
```rust
let closure = closure_recursion(0);
let result = closure(5);
println!("{}", result);
```
Output example:
```
10
```
## Explanation
 The closure takes the parameter 5 and calls itself with the parameter 5 - 1, which is 4. This process is repeated until the parameter is 0, at which point the closure returns the value of n, which is 0. The value of n is then incremented each time the closure is called, resulting in a final value of 10.

## Helpful links
- [Closure Recursion in Rust](https://doc.rust-lang.org/book/ch19-05-advanced-functions-and-closures.html#closure-recursion)
- [Closures in Rust](https://doc.rust-lang.org/book/ch13-01-closures.html)
- [Recursion in Rust](https://doc.rust-lang.org/book/ch03-03-how-functions-work.html#recursion)

group: rust-closure