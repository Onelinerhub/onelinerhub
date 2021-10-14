# How to read or change ith bit

```C
#define ithBit(num,i) ( (num & (1 << i) ) ? 1 : 0 )
#define onTheBit(num,i) (num | (1 << i) )
#define offTheBit(num,i) (num & ~(1 << i) )
#define changeBit(num,i,bit) (bit ? onTheBit(num,i) : offTheBit(num,i))
```

- ithBit - gives the ith bit of a number
- onTheBit - on the ith bit of a number
- offTheBit - off the ith bit of a number
- changeBit - will change the ith bit of a number to args bit

Note: Here index starts from right of the number and first bit is accessed using ithBit(num,0).

## Example
```C
#include <stdio.h>

// Snippet
#define ithBit(num,i) ( (num & (1 << i) ) ? 1 : 0 )
#define onTheBit(num,i) (num | (1 << i) )
#define offTheBit(num,i) (num & ~(1 << i) )
#define changeBit(num,i,bit) (bit ? onTheBit(num,i) : offTheBit(num,i))

int main(){
    int n = 45; // In binary 101101

    /* Reading the bits */
    printf("n 0th Bit: %d\n",ithBit(n,0));
    printf("n 1th Bit: %d\n",ithBit(n,1));

    /* Changing the bits */
    int changed_n1 = onTheBit(n,1); // It will change 101101 to 101111
    int changed_n2 = offTheBit(n,0); // It will change 101101 to 101100
    printf("n when 1th bit is on: %d\n",changed_n1);
    printf("n when 0th bit is off: %d\n",changed_n2);

    /* Changing the bits using variables */
    int new_bit1 = 0; // It should be 0 or 1
    int changed_n3 = changeBit(n,0,new_bit1); // Equivalent to offTheBit(n,0) and it will change 101101 to 101100

    int new_bit2 = 1;
    int changed_n4 = changeBit(n,4,new_bit2); // Equivalent to onTheBit(n,4) and it will change 101101 to 111101
    printf("n when 0th bit is off [using Variables]: %d\n",changed_n3);
    printf("n when 4th bit is on [Using Variables]: %d\n",changed_n4);

    return 0;
}
```
```
n 0th Bit: 1
n 1th Bit: 0
n when 1th bit is on: 47
n when 0th bit is off: 44
n when 0th bit is off [using Variables]: 44
n when 4th bit is on [Using Variables]: 61
```
