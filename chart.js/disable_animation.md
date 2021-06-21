# Disable start animation of charts

```javascript
new Chart('chart', {
  // ...
  options: { animation: { duration: 0 } }
});
```

- 'chart' - id of ```canvas``` element
- { duration: 0 } - setting animation duration to zero will disable it
