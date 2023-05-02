# Working with Slices in Rust

```rust
fn main() {
   let n1 = "Onelinerhub".to_string();
   println!("length of string: {}",n1.len());
   let c1 = &n1[4..9]; 

   println!("{}",c1);
}
```

- `"Tutorials".to_string()` - declares a String variable a1
- `let c1 = &n1[4..9];` - Creates a new string slice c1 that references a part of the original string n1. The range [4..9] specifies the start and end indices (inclusive) of the substring to be extracted from the original string. The & symbol is used to take a reference to the substring instead of creating a new String object.

```
length of string: 11
inerh
```

