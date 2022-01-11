# Calculate Euclidean distance in matlab

```matlab
function distance = euclideanDistance(x1, y1, x2, y2)
    distance = sqrt( ((x1 - y1) ^ 2) + ((x2 - y2) ^ 2) );
end
```