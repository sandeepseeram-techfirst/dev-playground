# Encryption 

Encryption works by encoding “plaintext” into “ciphertext,” typically through the use of cryptographic mathematical models known as algorithms.

### Symmetric encryption
also known as a shared key or private key algorithm, uses the same key for encryption and decryption. There is less of delay in decoding the data. 

### Asymmetric encryption 
also known as public-key cryptography, uses two separate keys to encrypt and decrypt data. One is a public key shared among all parties for encryption. Anyone with the public key can then send an encrypted message, but only the holders of the second, private key can decrypt the message. 


### Symmetric Encryption

1. DES (Data Encryption Standard)

- Created in the 1970s, adopted in 1977.

- Uses a 56-bit key → now too weak and outdated.

- Important historically because it inspired modern encryption methods.

2. 3DES (Triple DES)

- Improved DES by running it 3 times (encrypt–decrypt–encrypt).

- More secure than DES, but now also outdated and deprecated by NIST (since 2023).

3. AES (Advanced Encryption Standard)

- Most widely used today (adopted in 2001).

- Uses 128-bit blocks and key sizes of 128, 192, or 256 bits.

- Strong, fast, and secure → industry standard.

4. Twofish

- Very fast and supports keys up to 256 bits.

- Free to use (not patented), used in tools like PGP.

- Secure and efficient for both hardware and software.