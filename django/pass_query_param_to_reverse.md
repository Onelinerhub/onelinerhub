# How to use query param with reverse function

```python
"%s?param=parameter" % reverse("app_name:path_name")
```

- param - your query param name
- parameter - parameter value you want to pass to the path
- reverse - django function import (from django.shortcuts import reverse)
- path_name - name you give to a django path e.g. (path("path/", View.as_view(), name="path_name"))

## Example

```python
# urls.py
from django.urls import re_path
app_name = "example_app_name"
urlpatterns = [
    re_path(r"^example_path/$", View.as_view(), name="example_name")
]
# views.py
from django.shortcuts import reverse
print("%s?key=value" % reverse("example_app_name:example_name"))
```

```bash
/example_path/?key=value
```
