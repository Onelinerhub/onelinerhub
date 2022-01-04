# Read Matrix Data from .txt file

```matlab
function data = ReadMatrix(name)
    data = [];
    fid = fopen(name);
    if fid == -1
      disp(['File cannot be opened: ' name]);
      return;
    end;
    magic_word = uint8(fread(fid,8,'uint8'));
    magic = uint8('YANGVOCO');
    if sum(abs(magic_word(:) - magic(:))) ~= 0
      disp(['File format is wrong, magic: ' char(magic_word)]);
      return;
    end;
    n_column = double(fread(fid,1,'int32'));
    n_row = double(fread(fid,1,'int32'));
    data = zeros(n_row, n_column);
    for ii = 1:n_column
      tmp = double(fread(fid,n_row,'float32'));
      data(:, ii) = tmp(:);
    end;
    fclose(fid);
end
```