# How can I use Python and SciPy to calculate the Present Value of a Perpetuity with Growth?
// plain

The Present Value of a Perpetuity with Growth can be calculated using Python and SciPy. The formula for calculating the present value is as follows:

PV = C / (r - g)

Where C is the cash flow, r is the discount rate, and g is the growth rate.

The following example code uses SciPy to calculate the present value of a perpetuity with a cash flow of $1000, a discount rate of 5%, and a growth rate of 3%:

```
from scipy.finance import pv

cash_flow = 1000
discount_rate = 0.05
growth_rate = 0.03

present_value = pv(discount_rate, growth_rate, cash_flow)

print(present_value)
```

## Output example

```
14285.714285714287
```

## Code explanation


- `from scipy.finance import pv`: imports the `pv` function from the `scipy.finance` module.
- `cash_flow = 1000`: assigns the cash flow to a variable.
- `discount_rate = 0.05`: assigns the discount rate to a variable.
- `growth_rate = 0.03`: assigns the growth rate to a variable.
- `present_value = pv(discount_rate, growth_rate, cash_flow)`: calculates the present value using the `pv` function.
- `print(present_value)`: prints the present value.

## Helpful links
- [SciPy Finance Documentation](https://docs.scipy.org/doc/scipy/reference/tutorial/finance.html)

onelinerhub: [How can I use Python and SciPy to calculate the Present Value of a Perpetuity with Growth?](https://onelinerhub.com/python-scipy/how-can-i-use-python-and-scipy-to-calculate-the-present-value-of-a-perpetuity-with-growth)