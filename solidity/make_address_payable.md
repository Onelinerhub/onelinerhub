# Make address payable

```javascript
address addr1 = msg.sender;
address payable addr2 = address(uint160(addr1)); // Correct since Solidity >= 0.5.0
address payable addr3 = payable(addr1); // Correct since Solidity >= 0.6.0
```

- address addr1 = msg.sender; - addr1 is defined as the contract caller address
- address payable addr2 = address(uint160(addr1)); - addr2 is made payable. For Solidity versions >= 0.5.0
- address payable addr3 = payable(addr1); - addr2 is made payable. For Solidity versions >= 0.5.0
