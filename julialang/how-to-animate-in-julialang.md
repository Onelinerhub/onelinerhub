# How to animate in JuliaLang?
// plain

JuliaLang provides a powerful animation library called `Gtk.jl` which can be used to create animations.

```julia
using Gtk

# Create a window
win = GtkWindow("My Window", 400, 400)

# Create a canvas
canvas = GtkCanvas()

# Add the canvas to the window
push!(win, canvas)

# Create a circle
circle = GtkCircle(200, 200, 50)

# Add the circle to the canvas
push!(canvas, circle)

# Animate the circle
animate(circle, x=200, y=200, r=50, color="red", duration=2.0)
```

This code will create a window with a canvas and a circle in the center. The `animate` function will animate the circle by changing its `x`, `y`, `r` and `color` properties over a duration of 2 seconds.

Parts of the code:

- `using Gtk`: imports the Gtk library
- `GtkWindow`: creates a window
- `GtkCanvas`: creates a canvas
- `GtkCircle`: creates a circle
- `push!`: adds the canvas and circle to the window
- `animate`: animates the circle

## Helpful links

- [Gtk.jl Documentation](https://gtkjl.readthedocs.io/en/latest/)
- [JuliaLang Animation Tutorial](https://juliagraphics.github.io/Gtk.jl/latest/tutorials/animation.html)

onelinerhub: [How to animate in JuliaLang?](https://onelinerhub.com/julialang/how-to-animate-in-julialang)