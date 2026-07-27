This is a python implementation of the Diffie Hellman Key Exchange made to explore how it works and an implementation of the XOR cipher for basic message encryption

Each step should be pretty self explanatory

Only one user needs to generate and test values of P and G, of which should be shared with the other user.

Users should then exchange PUBLIC Keys.

Steps resume as shown in program.

For a value of P, built in prime generator present. If not using this, use a site like bigprimes.org (No longer recommended due to typical generation of unsuitable primes causing extremely high run times)

Plans moving forward:
- Integrated large prime number generation (COMPLETE)
- More efficient validation of the small generator with respect to P (COMPLETE)
- Increase the length of the generated secret key to reduce the effectiveness of frequency analysis based attacks (COMPLETE)
- Add a GUI with a more simplified flow through the program

Changes:
- Added SHA-256 Hash to Key before encryption / Decryption to increase the number of available characters before needing to reuse the key

Other than that pretty basic. Certainly serving as good practice

