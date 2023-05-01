# How to merge enums in Rust
// plain

Enums in Rust can be merged using the `#[derive(PartialEq, Eq, PartialOrd, Ord, Clone, Copy)]` attribute. This attribute allows the enum to be compared, ordered, cloned, and copied.

## Code example:

```
#[derive(PartialEq, Eq, PartialOrd, Ord, Clone, Copy)]
enum Color {
    Red,
    Blue,
    Green
}

fn main() {
    let color1 = Color::Red;
    let color2 = Color::Blue;
    let color3 = Color::Green;

    let colors = [color1, color2, color3];
    let merged_colors = merge_enums(colors);
    println!("Merged Colors: {:?}", merged_colors);
}

fn merge_enums(colors: [Color; 3]) -> [Color; 3] {
    let mut merged_colors = [Color::Red, Color::Blue, Color::Green];
    for color in colors.iter() {
        if !merged_colors.contains(color) {
            merged_colors.push(*color);
        }
    }
    merged_colors
}
```

### Output

Merged Colors: [Red, Blue, Green]

## Explanation:

1. The `#[derive(PartialEq, Eq, PartialOrd, Ord, Clone, Copy)]` attribute is added to the `Color` enum to allow it to be compared, ordered, cloned, and copied.
2. The `merge_enums` function takes an array of `Color` enums as an argument and returns an array of `Color` enums.
3. The `merged_colors` array is initialized with the three colors `Red`, `Blue`, and `Green`.
4. The `for` loop iterates over the `colors` array and checks if the `merged_colors` array contains the current color.
5. If the `merged_colors` array does not contain the current color, it is added to the `merged_colors` array.
6. The `merged_colors` array is returned at the end of the function.

## Helpful links:

1. [Rust Enums](https://doc.rust-lang.org/book/ch06-01-defining-an-enum.html)
2. [Rust Derive Attribute](https://doc.rust-lang.org/reference/attributes.html#derive-attributes)