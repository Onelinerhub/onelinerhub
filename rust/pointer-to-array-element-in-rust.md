# Pointer to array element in Rust
// plain

In Rust, a pointer to an array element is created using the `&` operator. For example, to create a pointer to the first element of an array `arr`, the syntax would be `&arr[0]`. This pointer can then be used to access the element, or to pass it to a function. Additionally, the `std::slice::from_raw_parts` function can be used to create a slice from a pointer to an array element. This function takes a pointer and a length as arguments, and returns a slice of the array starting from the pointer. For example, `std::slice::from_raw_parts(&arr[0], arr.len())` would create a slice of the entire array.

group: rust-pointers