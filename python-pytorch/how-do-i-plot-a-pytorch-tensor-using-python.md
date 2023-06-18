# How do I plot a PyTorch tensor using Python?
// plain

To plot a PyTorch tensor using Python, we can use the matplotlib library. Matplotlib is a plotting library for Python which provides a variety of plots, such as line plots, histograms, bar charts, etc.

## Example code

```
import matplotlib.pyplot as plt

# Create a PyTorch tensor
x = torch.rand(10)

# Plot the tensor
plt.plot(x.numpy())
plt.show()
```

## Output example


![Example Output](https://i.imgur.com/4J2V7hH.png)

## Code explanation


1. `import matplotlib.pyplot as plt`: This imports the matplotlib library and assigns it to the variable `plt`.
2. `x = torch.rand(10)`: This creates a PyTorch tensor with 10 random values.
3. `plt.plot(x.numpy())`: This plots the tensor using the matplotlib library.
4. `plt.show()`: This displays the plot.

## Helpful links

- [Matplotlib Documentation](https://matplotlib.org/3.2.1/contents.html)
- [PyTorch Tutorials](https://pytorch.org/tutorials/)

onelinerhub: [How do I plot a PyTorch tensor using Python?](https://onelinerhub.com/python-pytorch/how-do-i-plot-a-pytorch-tensor-using-python)