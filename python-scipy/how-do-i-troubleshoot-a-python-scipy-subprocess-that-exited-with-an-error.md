# How do I troubleshoot a Python Scipy subprocess that exited with an error?
// plain

1. First, identify the source of the error. Check the output of the subprocess to see what the error is.
2. Check the code for syntax errors. If the error is a syntax error, correct the code and re-run the subprocess.
3. Check the command line arguments. Make sure the arguments provided to the subprocess are valid.
4. Check the environment variables. Make sure the environment variables are set correctly.
5. Check the input data. Make sure the data provided to the subprocess is valid.
6. Debug the code. Use a debugging tool such as pdb or the Python debugger to step through the code and identify the source of the error.
7. If the error persists, check the Scipy documentation or ask for help on the Scipy mailing list.

```
import subprocess

proc = subprocess.Popen(['my_script.py', 'arg1', 'arg2'], stdout=subprocess.PIPE)
out, err = proc.communicate()

if err:
    print('Error:', err)
```

## Output example


`Error: b'SyntaxError: invalid syntax\n'`

onelinerhub: [How do I troubleshoot a Python Scipy subprocess that exited with an error?](https://onelinerhub.com/python-scipy/how-do-i-troubleshoot-a-python-scipy-subprocess-that-exited-with-an-error)