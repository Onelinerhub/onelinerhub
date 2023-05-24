# How to install JuliaLang on Linux?
// plain

Installing JuliaLang on Linux is easy and straightforward.

1. Download the latest version of Julia from the [JuliaLang website](https://julialang.org/downloads/).
2. Extract the downloaded file using the command `tar -xzf julia-<version>.tar.gz`
3. Move the extracted folder to the desired location using the command `mv julia-<version> <desired_location>`
4. Add the Julia binary to the PATH environment variable using the command `export PATH="$PATH:<desired_location>/julia-<version>/bin"`
5. Verify the installation by running the command `julia` in the terminal.

```
$ julia
               _
   _       _ _(_)_     |  Documentation: https://docs.julialang.org
  (_)     | (_) (_)    |
   _ _   _| |_  __ _   |  Type "?" for help, "]?" for Pkg help.
  | | | | | | |/ _` |  |
  | | |_| | | | (_| |  |  Version 1.4.2 (2020-05-23)
 _/ |\__'_|_|_|\__'_|  |  Official https://julialang.org/ release
|__/                   |

julia>
```

onelinerhub: [How to install JuliaLang on Linux?](https://onelinerhub.com/julialang/how-to-install-julialang-on-linux)