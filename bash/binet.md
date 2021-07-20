# Binet's Formula in bash
There is no iteration or recursion with this method

```bash
export n=1000 && export PHI="1.618033988749894848204586834365638117720309179805762862135448622705260462818902449707207204189391137484754088075386891752126633862223536931793180060766726354433389086595939582905638322661319928290267880675208766892501711696" && export PSI=$(echo "1 - $PHI" | bc) && echo "Calculating Fn($n) via Binet's Formula" && 
if [ $n -le 2 ]; then echo "( ($PHI^$n - $PSI^$n) / ($PHI - $PSI) )" | bc;
else time echo "( ($PHI^$n - $PSI^$n) / ($PHI - $PSI) + 1 )" | bc; fi;
```

- export n - where n is the Fibonacci value to calculate
- PHI= - export PHI and PSI values (for higher n values increase the decimal places of `PHI`)
- Fn($n) - is calculated via [Binet's Formula](https://en.wikipedia.org/wiki/Fibonacci_number#Binet's_formula)
- | bc - Binet's Formula is piped to bc, the bash calculator
- ($PHI - $PSI) + 1 - Have to do some trickery with rounding by adding 1
