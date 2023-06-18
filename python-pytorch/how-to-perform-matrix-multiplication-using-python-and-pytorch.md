# How to perform matrix multiplication using Python and PyTorch?
// plain

Matrix multiplication can be performed using Python and PyTorch. To do so, you first need to create two matrices and define them as tensors. Then, use the `torch.mm()` method to perform the matrix multiplication.

```python
import torch

# Create two matrices and define them as tensors
matrix_a = torch.tensor([[1,2],
                        [3,4]])

matrix_b = torch.tensor([[5,6],
                        [7,8]])

# Perform the matrix multiplication
matrix_c = torch.mm(matrix_a, matrix_b)

print(matrix_c)
```
## Output example

```
tensor([[19, 22],
        [43, 50]])
```

The code above consists of the following parts:
1. `import torch` - This imports the PyTorch library.
2. `matrix_a = torch.tensor([[1,2], [3,4]])` - This creates a matrix with the values `1,2,3,4` and defines it as a tensor.
3. `matrix_b = torch.tensor([[5,6], [7,8]])` - This creates a matrix with the values `5,6,7,8` and defines it as a tensor.
4. `matrix_c = torch.mm(matrix_a, matrix_b)` - This performs the matrix multiplication of `matrix_a` and `matrix_b` and stores the result in `matrix_c`.
5. `print(matrix_c)` - This prints the result of the matrix multiplication to the console.

## Helpful links
- [PyTorch Documentation](https://pytorch.org/docs/stable/)
- [Matrix Multiplication in PyTorch](https://pytorch.org/tutorials/beginner/blitz/tensor_tutorial.html#sphx-glr-beginner-blitz-tensor-tutorial-py)

onelinerhub: [How to perform matrix multiplication using Python and PyTorch?](https://onelinerhub.com/python-pytorch/how-to-perform-matrix-multiplication-using-python-and-pytorch)