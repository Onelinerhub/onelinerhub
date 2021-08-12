# Pseudo random number generation

Note: True random number generatio without using oracles isnt possible

```javascript
uint8 number = uint8(uint256(keccak256(abi.encodePacked(block.timestamp, block.difficulty)))%251);
```

- uint8( - converts everything to uint8
- uint256( - needs to be converted for bytes32 and int_const to interact
- keccak256(abi.encodePacked(block.timestamp, block.difficulty))) - takes the block hash and difficulty, ABI encodes it, and hashes it with keccak256
- %251); - defines the max number. In this case its 250

## Example
```javascript
pragma solidity >=0.7.0 <0.9.0;

contract randomNumber {

    uint8 public number;
    
    function store() public {
        number = uint8(uint256(keccak256(abi.encodePacked(block.timestamp, block.difficulty)))%251);
    }
}
```
