# How can I use Python Scipy to generate random numbers?
// plain

Scipy is a python library that contains a variety of modules for scientific computing. It provides functions for generating random numbers from various distributions.

One way to generate random numbers using Scipy is to use the `scipy.stats.uniform` function. This function will generate random numbers from a uniform distribution between two given numbers.

For example, to generate 10 random numbers between 1 and 10, you can use the following code:

```
from scipy.stats import uniform

# Generate 10 random numbers between 1 and 10
rand_nums = uniform.rvs(size=10, loc=1, scale=10)
print(rand_nums)
```

## Output example

```
[7.81910238 4.7351252  5.52031802 8.72389741 8.81722884 5.71712097
 2.08716585 8.96568159 9.1212093  7.94477239]
```

The code above consists of the following parts:

1. `from scipy.stats import uniform`: This imports the `uniform` module from the `scipy.stats` library.
2. `uniform.rvs(size=10, loc=1, scale=10)`: This generates 10 random numbers from a uniform distribution between 1 and 10. The `size` argument is used to specify the number of random numbers to generate, the `loc` argument is used to specify the lower limit of the range, and the `scale` argument is used to specify the upper limit of the range.
3. `print(rand_nums)`: This prints the generated random numbers.

For more information about generating random numbers using Scipy, see [this page](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.uniform.html).

onelinerhub: [How can I use Python Scipy to generate random numbers?](https://onelinerhub.com/python-scipy/how-can-i-use-python-scipy-to-generate-random-numbers)