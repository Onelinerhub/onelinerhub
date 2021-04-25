# Add swap

```bash
fallocate -l 2G /swapfile && chmod 600 /swapfile && mkswap /swapfile && swapon /swapfile
```

- -l 2G - required size of your swap file
- /swapfile - path to the swap file itself
