# ElGamal Encryption Algorithm
ElGamal encryption system is an asymmetric key encryption algorithm for public-key cryptography. It was described in the 20th century by an Egyptian cryptographer and entrepreneur Dr. Taher ElGamal. (https://en.wikipedia.org/wiki/ElGamal_encryption)

## Algorithm description
The problem of a discret logarithm is a foundation of ElGamal encryption system security. The algorith works correctly into the multiplicative groups of modulo p, where p is a large prime number. The concrete steps of the alogirthm was described in a "Handbook of Applied Cryptography", that I heartily recommend. (https://cacr.uwaterloo.ca/hac/)

## Implementation
The implementation was created in Python programming language. At the begining I had to implement three additional functions, that are necessary to the execution of ElGamal encryption algorithm. These functions deal with problems such as:

* Generating a large prime number
* Operation of modular exponentiation
* Finding a generator of a multiplicative group

Afterwards it was possible to build key generator, encryption and decryption functions. The algorithm does not include the coversion method so in conclusion the program requires to enter an integer representation of our messege. There are many ways to solve this problem, for example with the use of ASCII system. In my implementation I decided to leave this issue open.

To start the program we have to enter the interval of a prime number and an integer representation of the messege. 
