# How to validate an IP using Python regex?
// plain

Python regex can be used to validate an IP address. The following example code block uses regex to validate an IP address:
```
import re

def validate_ip(ip):
    regex = '''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)'''
    if(re.search(regex, ip)):
        print("Valid IP")
    else:
        print("Invalid IP")

ip = "192.168.1.1"
validate_ip(ip)
```
The output of the example code is:
```
Valid IP
```
## Code explanation

1. `import re`: This imports the `re` module which provides regular expression matching operations.
2. `regex = '''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)'''`: This defines the regex pattern which is used to validate the IP address.
3. `if(re.search(regex, ip)):`: This uses the `re.search()` method to search for the regex pattern in the given IP address.
4. `print("Valid IP")`: This prints the output if the IP address is valid.
5. `print("Invalid IP")`: This prints the output if the IP address is invalid.

## Helpful links
- [Python Regular Expression](https://www.w3schools.com/python/python_regex.asp)
- [Python re Module](https://docs.python.org/3/library/re.html)

onelinerhub: [How to validate an IP using Python regex?](https://onelinerhub.com/python-regex/how-to-validate-an-ip-using-python-regex)