#imports
import random
import math
import hashlib
import tkinter as tk
p = 0

#sub-programs
def get_30_digit_prime():
    def is_prime(n, k=40):
        if n in (2, 3): return True
        if n % 2 == 0 or n < 2: return False
        r, d = 0, n - 1
        while d % 2 == 0:
            r += 1
            d //= 2
        for _ in range(k):
            a = random.randint(2, n - 2)
            x = pow(a, d, n)
            if x == 1 or x == n - 1: continue
            for _ in range(r - 1):
                x = pow(x, 2, n)
                if x == n - 1: break
            else: return False
        return True

    while True:
        num = random.randint(10**29, (10**30) - 1)
        if num % 2 != 0 and is_prime(num):
            return num

def autoPGen():
    P = get_30_digit_prime()
    print("The generated prime number is: ", P)

def internal_miller_rabin(n, k=5):
    if n < 2: return False
    for p_base in [2, 3, 5, 7, 11, 13, 17, 19, 23]:
        if n == p_base: return True
        if n % p_base == 0: return False
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1: continue
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1: break
        else: return False
    return True

def pollard_rho(n):
    if n % 2 == 0: return 2
    if internal_miller_rabin(n): return n
    x = random.randint(2, n - 1)
    y = x
    c = random.randint(1, n - 1)
    g = 1
    while g == 1:
        x = (pow(x, 2, n) + c) % n
        y = (pow(y, 2, n) + c) % n
        y = (pow(y, 2, n) + c) % n
        g = math.gcd(abs(x - y), n)
    return g

def get_prime_factors(n):
    factors = set()
    queue = [n]
    while queue:
        curr = queue.pop()
        if curr == 1: continue
        if internal_miller_rabin(curr):
            factors.add(curr)
        else:
            factor = pollard_rho(curr)
            queue.append(factor)
            queue.append(curr // factor)
    return factors

def manPGCheck():
    P = int(input("Please enter a prime number: "))
    phiP = P - 1
    G = int(input("Please enter a potential primitive root: "))
    
    factors = get_prime_factors(phiP)

    is_primitive = True
    for q in factors:
        testPower = phiP // q
        if pow(G, testPower, P) == 1:
            is_primitive = False
            break

    if is_primitive:
        print(f"Your values are: P = {P}, G = {G}")
        print("Share these values with the other user.")
    else:
        print(f"{G} is not a primitive root of {P}! Try again with another value ")
                    
def sharedPGGen():
##    def primRoots(modulo):
##        required_set = {num for num in range(1, modulo) if bltin_gcd(num, modulo) }
##        return [g for g in range(1, modulo) if required_set == {pow(g, powers, modulo)
##            for powers in range(1, modulo)}]
##    print(primRoots(p))

    
    def gcd(a,b):
        while b != 0:
            a, b = b, a % b
        return a

    def primRoots(modulo):
        global roots
        roots = []
        required_set = set(num for num in range (1, modulo) if gcd(num, modulo) == 1)
        count = 1
        for g in range(1, modulo):
            
            actual_set = set(pow(g, powers) % modulo for powers in range (1, modulo))
            print("Iterations Completed: ", count)
            count = count + 1
            if roots.count(int) > 2:
                break
            if required_set == actual_set:
                roots.append(g)
            if len(roots) > 0:
                break
                
        return roots

    
    p = int(input("Please enter a prime number: "))
    print("Please wait whilst your number is processed. This may take a while.")
    primitive_roots = primRoots(p)
    chosenRoot = primitive_roots[0]
    print("Your values are: P = ", p, "G = ", chosenRoot)
    print("Share these values with the other user.")

def pubKeyGen():
    desiredPrivateKey = random.randint(100000000000000000000000000, 99999999999999999999999999999)
    enteredSharedP = int(input("Please enter the shared P value: "))
    enteredG = int(input("Please enter the shared G value: "))
    Y = pow(enteredG, desiredPrivateKey, enteredSharedP)
    print("Your public key is: ", Y)
    print("Your Private key is: ", desiredPrivateKey)
    print("Ensure to NEVER share your private key.")
    print("You now need to send your PUBLIC key to the other user")

def sharedKeyCalc():
    receivedPubKey = int(input("Please enter the public key you have received from the other user: "))
    enteredPrivKey = int(input("Please enter your PRIVATE key: "))
    enteredPValue = int(input("Please enter the shared P value: "))
    K = pow(receivedPubKey, enteredPrivKey, enteredPValue)
    #K value to be made as long as possible to prevent frequency analysis.
    print("Your Shared Secret Key is: ", K)
    print("The other user will have this value.")
    print("You can use this value to encrypt messages")
    print("Take care to NEVER share this key.")

def messageEncryption():
    msg = (input("Please enter your message: "))
    key = (input("Please enter the shared secret key: "))

    sha256 = hashlib.sha256()
    sha256.update(key.encode())
    keyHash = sha256.hexdigest()
    addToEnBin = ""
    binMessage = "".join(format(ord(char), '08b') for char in msg)
    
    binKey = format(int(keyHash, 16), '0256b')
    requiredKeys = (binKey * (len(binMessage) // len(binKey) + 1))[:len(binMessage)]

    for i in range(len(binMessage)):
        if binMessage[i] == requiredKeys[i]:
            addToEnBin = addToEnBin + "0"
        else:
            addToEnBin = addToEnBin + "1"
            
    num = int(addToEnBin, 2)
    hex_length = (len(binMessage) + 3) // 4
    hexNum = format(num, f'0{hex_length}x')
    hexNum = hexNum.upper()
    print("Your encrypted message is: ", hexNum)

def messageDecryption():
    msg = (input("Please enter the received message: ")).strip().lower()
    key = (input("Please enter the shared secret key: "))
    addToEnBin = ""
    sha256 = hashlib.sha256() 
    sha256.update(key.encode())
    keyHash = sha256.hexdigest()
    key = keyHash
    key = key.upper()
    
    # FIXED: Convert hex cleanly back into bits matching the exact length of the hex string
    bit_length = len(msg) * 4
    binMessage = format(int(msg, 16), f'0{bit_length}b')
    
    # MATCHED: Uses the exact same 256-bit raw key format as the updated encryption routine
    binKey = format(int(keyHash, 16), '0256b')
    requiredKeys = (binKey * (len(binMessage) // len(binKey) + 1))[:len(binMessage)]
    
    for i in range(len(binMessage)):
        if binMessage[i] == requiredKeys[i]:
            addToEnBin = addToEnBin + "0"
        else:
            addToEnBin = addToEnBin + "1"
            
    s = ''.join(chr(int(addToEnBin[i:i+8], 2)) for i in range(0, len(addToEnBin), 8))
    print("Your decrypted Message is: ", s)
#main program
while True:
    print("Please select an option from the menu below by entering the number.")
    userChoice = int(input("""1. Generate a Large Prime Number (P)
2. Test values for accceptable G values
3. Generate your Public and Private keys
4. Establish the Shared Secret Key
5. Encrypt a message    
6. Decrypt a message    
Choice: """))

    if userChoice == 2:
        manPGCheck()
    elif userChoice == 3:
        pubKeyGen()
    elif userChoice == 4:
        sharedKeyCalc()
    elif userChoice == 5:
        messageEncryption()
    elif userChoice == 6:
        messageDecryption()
    elif userChoice == 1:
        autoPGen()
    
        
    else:
        print("The number you have entered is not a valid option")
