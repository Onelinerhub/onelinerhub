# Prevent reentrancy attacks

Reentrancy attacks are a common pitfall in smart contract development. They are most commonly used to steal funds form unsuspecting users.

```javascript
bool internal locked;
modifier noReentrancy() {
    require(!locked, "No reentrancy!"); locked = true; _; locked = false;
}
```

- bool internal locked; - An internal variable with the current contract state needs to be defined
- modifier noReentrancy()  - A modifier is created so that it can be easily appended to functions
- require(!locked, "No reentrancy!"); - When a function with this modifier is executed, it checks if the contract is locked. If it is, it reverts execution.
- locked = true; _; locked = false; -  The contract is locked, the function called is ran, and after execution the contract is unlocked.   

## Example
```javascript
pragma solidity >=0.7.0 <0.9.0;

contract Reenctancy {

    uint256 public number;
    

    bool internal locked;
    modifier noReentrancy() {
        require(!locked, "No reentrancy!"); locked = true; _; locked = false;
    }


    function store(uint256 num) public noReentrancy(){
        number = num;
    }
}
```
