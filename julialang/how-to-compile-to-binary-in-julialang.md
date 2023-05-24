# How to compile to binary in JuliaLang?
// plain

JuliaLang is a high-level, high-performance programming language. It can be used to compile code into a binary executable. To do this, you need to use the `ccall` function. This function takes a function name, a return type, and a list of argument types as arguments.

## Example

```julia
ccall((:my_function, "my_library.so"), Int32, (Int32, Int32), arg1, arg2)
```

This example calls the function `my_function` from the library `my_library.so`, with two `Int32` arguments, `arg1` and `arg2`. It returns an `Int32` value.

Parts of the code:
- `ccall`: The function used to call a function from a library.
- `(:my_function, "my_library.so")`: The function name and library name.
- `Int32`: The return type of the function.
- `(Int32, Int32)`: The argument types of the function.
- `arg1` and `arg2`: The arguments passed to the function.

## Helpful links
- [JuliaLang Documentation](https://docs.julialang.org/en/v1/)
- [ccall Function Documentation](https://docs.julialang.org/en/v1/base/c/index.html#Calling-C-Functions-1)

onelinerhub: [How to compile to binary in JuliaLang?](https://onelinerhub.com/julialang/how-to-compile-to-binary-in-julialang)