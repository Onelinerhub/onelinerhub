# Calculate Euclidean distance

```matlab
function distance = euclideanDistance(x1, y1, x2, y2)
    distance = sqrt( ((x1 - y1) ^ 2) + ((x2 - y2) ^ 2) );
end
```

- `euclideanDistance` - name of the function that will be used later
- `sqrt` - square root
- ``(x1 - y1) ^ 2`` - square of coordinate difference of first point
- ``(x2 - y2) ^ 2`` - square of coordinate difference of second point


