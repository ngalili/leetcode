# Python program to demonstrate working of HashTable 
# A good hash function has the following characteristics:
# 1. should not generate keys that are too large and the bucket space is small. Space is wasted. 
# 2. keys generated should be neither very close nor too far in range.
# 3. the collision must be minimized as much as possible

hashTable = [[],] * 10

def checkPrime(n):
    if n == 1 or n == 0:
        return 0
    
    for i in range(2, n//2):
        if n % i == 0:
            return 0

    return 1

def getPrime(n):
    if n % 2 == 0:
        n += 1

    while not checkPrime(n):
        n += 2
    
    return n

def hashFunction(key):
    capacity = getPrime(10)
    return key % capacity

def insertData(key, data):
    index = hashFunction(key)
    hashTable[index] = [key, data]

def removeData(key):
    index = hashFunction(key)
    hashTable[index] = 0

insertData(123, "apple")
insertData(432, "mango")
insertData(213, "banana")
insertData(654, "pineapple")

print(hashTable)

removeData(123)

print(hashTable)