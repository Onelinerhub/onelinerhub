# Write matrix data to a text file

```matlab
function SaveMatrix(data, name)
    fid = fopen(name, 'w');
    [n_row, n_column] = size(data);
    magic = uint8('YANGVOCO');
    fwrite(fid, magic, 'uint8');
    fwrite(fid, n_column, 'int32');
    fwrite(fid, n_row, 'int32');
    for ii = 1:n_column
      fwrite(fid, data(:, ii), 'float32');
    end;
    fclose(fid);
end
```

- `SaveMatrix` - function for saving matrix to a specified file
- `name` - path of the file to save matrix to
- `fopen` - opens specified file for writing

group: matrix_txt


