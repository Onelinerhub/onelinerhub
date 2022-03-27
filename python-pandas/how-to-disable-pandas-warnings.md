# How to disable Pandas warnings

```python
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import pandas as pd
# ...
```

- `import warnings` - load module to manage warnings
- `warnings.simplefilter` - filter warnings based on specified rules
- `ignore` - just ignore all warnings
- `FutureWarning` - type of warning to ignore
- `import pandas as pd` - load [lib:Pandas module](/python-pandas/how-to-install-pandas)


