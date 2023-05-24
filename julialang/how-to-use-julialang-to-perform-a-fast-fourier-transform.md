# How to use JuliaLang to perform a Fast Fourier Transform?
// plain

JuliaLang provides a package called `FFTW` to perform Fast Fourier Transform (FFT). To use it, first install the package by running `Pkg.add("FFTW")` in the Julia REPL. Then, import the package by running `using FFTW` in the Julia REPL.

To perform a FFT, use the `fft` function. For example, to perform a FFT on a vector `x`, run `y = fft(x)`.

```
julia> using FFTW

julia> x = [1,2,3,4]
4-element Array{Int64,1}:
 1
 2
 3
 4

julia> y = fft(x)
4-element Array{Complex{Float64},1}:
 10.0+0.0im
  -2.0+2.0im
  -2.0+0.0im
  -2.0-2.0im
```

## Code explanation


- `Pkg.add("FFTW")`: install the `FFTW` package
- `using FFTW`: import the `FFTW` package
- `fft(x)`: perform a FFT on a vector `x`

## Helpful links

- [FFTW.jl](https://github.com/JuliaMath/FFTW.jl)

onelinerhub: [How to use JuliaLang to perform a Fast Fourier Transform?](https://onelinerhub.com/julialang/how-to-use-julialang-to-perform-a-fast-fourier-transform)