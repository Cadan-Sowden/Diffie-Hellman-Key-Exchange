#imports
import random
p = 0
#sub programs



def get_25_digit_prime():
    def is_prime(n, k=40):
        # Internal helper for the Miller-Rabin primality test
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

    # Main loop to find the prime
    while True:
        # Generates a random number with exactly 25 digits
        num = random.randint(10**24, (10**25) - 1)
        # Fast pre-check: skip even numbers
        if num % 2 != 0 and is_prime(num):
            return num





def autoPGen():
    P = get_25_digit_prime()
    print("The generated prime number is: ", P)

def manPGCheck():
    P = int(input("Please enter a prime number: "))
    phiP = P - 1
    G = int(input("Please enter a potential primitive root: "))
    print("""Please wait..."
If waiting for over 30 seconds / 1 minute, it may be worth terminating the program and trying a different value of G.""")
    factors = []
    nList = []
    flag = False

    n = phiP
    if n >= 2:
        while n % 2 == 0:
            factors.append(2)
            n //= 2
  
    # Check odd factors from 3 up to the square root of n.
    i = 3
    while i < n // i:
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 2

    # If n is still greater than 1, it must be a prime factor.
    if n > 1:
        factors.append(n)   
    for i in range(len(factors)):
        n = int(phiP / factors[i-1])
        nList.append(n)

    for i in range(len(nList)):
        testPower = nList[i-1]
        residue = pow(G, testPower, P)
        if residue == 1:
            flag = True

    if flag == False:
        print("Your values are: P = ", P, "G = ", G)
        print("Share these values with the other user.")
    if flag == True:
        print("G is not a primitive root of P! Try again with another value of G.")
        


        
            
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
    desiredPrivateKey = random.randint(100000000000000000, 99999999999999999999)
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
    print("Your Shared Secret Key is: ", K)
    print("The other user will have this value.")
    print("You can use this value to encrypt messages")
    print("Take care to NEVER share this key.")

def messageEncryption():
    BinList = []
    temp = ""
    encryptBinary = []
    addToEnBin = ""
    msg = (input("Please enter your message: "))
    key = (input("Please enter the shared secret key: "))
    binMessage = "".join(format(ord(char), '08b') for char in msg)
    binKey = "".join(format(ord(char), '08b') for char in key)
    requiredKeys = binKey * (len(binMessage) // 8)  
    for i in range(len(binMessage)):
        if binMessage[i] == requiredKeys[i]:
            addToEnBin = addToEnBin + "0"
        else:
            addToEnBin = addToEnBin + "1"
    num = int(addToEnBin, 2)
    hexNum = hex(num).upper()
    print("Your encrypted Message is: ", hexNum[2:])

            
        

def messageDecryption():
    msg = (input("Please enter the received message: "))
    key = (input("Please enter the shared secret key: "))
    addToEnBin = ""
    binMessage = format(int(msg, 16), 'b')
    binMessage = "0" + binMessage
    binKey = "".join(format(ord(char), '08b') for char in key)
    requiredKeys = binKey * (len(binMessage) // 8)
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
