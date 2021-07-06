# Make chart start from zero value

```javascript
new Chart('chart', {
  // ...
  options: { |{|scales: { y: { min: 0 } }|}| }
});
```

- 'chart' - id of ```canvas``` element
- y: { min: 0 } - override minimum value for ```y``` axis to make it start from zero
