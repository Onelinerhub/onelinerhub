# How to merge hashsets in Rust
// plain

Hashsets in Rust can be merged using the `union` method. This method takes two hashsets as arguments and returns a new hashsets containing all the elements from both the hashsets.

## Code example:
```
let mut hs1 = HashSet::new();
hs1.insert(1);
hs1.insert(2);
hs1.insert(3);

let mut hs2 = HashSet::new();
hs2.insert(3);
hs2.insert(4);
hs2.insert(5);

let hs3 = hs1.union(&hs2);

println!("{:?}", hs3);
```

### Output
`HashSet { 1, 2, 3, 4, 5 }`

Explanation:
- `let mut hs1 = HashSet::new();`: This line creates a new hashsets called `hs1`
- `hs1.insert(1);`: This line inserts the element `1` into the hashsets `hs1`
- `let mut hs2 = HashSet::new();`: This line creates a new hashsets called `hs2`
- `hs2.insert(3);`: This line inserts the element `3` into the hashsets `hs2`
- `let hs3 = hs1.union(&hs2);`: This line creates a new hashsets called `hs3` which contains all the elements from both the hashsets `hs1` and `hs2`
- `println!("{:?}", hs3);`: This line prints the contents of the hashsets `hs3`

## Helpful links:
- [Rust Documentation - HashSet](https://doc.rust-lang.org/std/collections/struct.HashSet.html)
- [Rust Documentation - union](https://doc.rust-lang.org/std/collections/struct.HashSet.html#method.union)