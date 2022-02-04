# How to extract ZIP file

### We'll use [zip lib](https://luarocks.org/modules/brimworks/lua-zip) to load file contents from zip archive:

```lua
zip = require 'brimworks.zip'

local zip_arc = zip.open('/tmp/file.zip')
local file = zip_arc:open(zip_arc:get_num_files())
local stat = zip_arc:stat(zip_arc:get_num_files())
str = file:read(stat.size)

zip_arc:close()
```

- `require 'brimworks.zip'` - load [zip lib](https://onelinerhub.com/lua/install-zip-module-with-luarocks)
- `zip.open` - create existing zip archive to extract file from
- `zip_arc:open` - open specified file from archive (using its index)
- `zip_arc:get_num_files()` - get number of files in zip archive (assume there's one file, then we'll get `1`)
- `zip_arc:stat` - return specified file stats to get decompressed file size
- `file:read` - read file contents limited by a given value
- `stat.size` - we're asking to read full length of compressed file content
- `str` - variable will contain uncompressed file contents from zip archive

group: zip

## Example: 
```lua
zip = require 'brimworks.zip'

local zip_arc = zip.open('/tmp/file.zip')
local file = zip_arc:open(zip_arc:get_num_files())
local stat = zip_arc:stat(zip_arc:get_num_files())
str = file:read(stat.size)

print(str)

zip_arc:close()
```
```
1
2
3
4
1
2
3
4
5
1
21
123
4
1
1
2
3
1
12



```

