## Print in italics!

This works with Python **3.6+**

``` python

#!/usr/bin/env python3

import os

#Install quo from PypI
os.system("pip install quo==2021.3.5")

## Import quo module

import quo
from quo import echo
echo(f"Hello World!", fg="cyan", italic=True)

```
