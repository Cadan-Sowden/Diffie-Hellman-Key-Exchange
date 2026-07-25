#imports
import random
#sub programs
def manPGCheck():
    P = int(input("Please enter a prime number: "))
    phiP = P - 1
    G = int(input("Please enter a potential primitive root: "))
    print("Please wait...")
    factors = []
    nList = []
    flag = False
##    while True:
##        enteredFactor = int(input("Please enter the prime factors of P - 1. Enter 1 to exit: "))
##        if enteredFactor == 1:
##            break
##        else:
##            factors.append(enteredFactor)
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
    userChoice = int(input("""1. Generate shared P and G values
2. Generate your Public and Private keys
3. Establish the Shared Secret Key
4. Encrypt a message    
5. Decrypt a message    
Choice: """))

    if userChoice == 1:
        manPGCheck()
    elif userChoice == 2:
        pubKeyGen()
    elif userChoice == 3:
        sharedKeyCalc()
    elif userChoice == 4:
        messageEncryption()
    elif userChoice == 5:
        messageDecryption()
    
        
    else:
        print("The number you have entered is not a valid option")
