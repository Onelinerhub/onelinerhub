# Append value to list using lpush

```lua
local redis = (require 'redis').connect('127.0.0.1', 6379)
redis:push('list1', 'a')
```


group: list

```



lua: /tmp/test.lua:2: attempt to call a nil value (method 'push')
stack traceback:
	/tmp/test.lua:2: in main chunk
	[C]: in ?
```

