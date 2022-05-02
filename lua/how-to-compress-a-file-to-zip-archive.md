# How to compress a file to ZIP archive

### We'll use [lib:zip lib](https://onelinerhub.com/lua/install-zip-module-with-luarocks) to create zip archive from file:

```lua
zip = require 'brimworks.zip'

local zip_arc = zip.open('/tmp/file.zip', zip.CREATE)
file_idx = zip_arc:add('test.txt', "file", '/tmp/test.txt')

zip_arc:close()
```

- `require 'brimworks.zip'` - load [lib:zip lib](https://onelinerhub.com/lua/install-zip-module-with-luarocks)
- `zip.open` - create new zip archive
- `/tmp/file.zip` - name of the archive to create
- `zip_arc:add` - adds new file to zip archive
- `test.txt` - name of the file in zip archive (you can choose any name)
- `"file"` - type of the object in archive (file in our case as we will compress file)
- `'/tmp/test.txt'` - path to file to compress and save in our archive
- `zip_arc:close()` - close archive handler to write changes on disk

group: zip

## Example: 
```lua
zip = require 'brimworks.zip'
os.remove('/tmp/file.zip');
local zip_arc = zip.open('/tmp/file.zip', zip.CREATE)
file_idx = zip_arc:add('test.txt', "file", '/tmp/test.txt')
zip_arc:close()
```

link_youtube: https://youtu.be/_RST73dkPjE
