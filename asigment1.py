
#Q1
def factorial(n):
    if n<0:
      print("Negative number please enter a positive number")
    else:

     if n == 0:
        return 1
     else:
        return n * factorial(n-1)
print(factorial(4))

#Q2

def count_upper_lower(string):
    upper_count = 0
    lower_count = 0
    
    for char in string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    
    print("No. of Upper case characters:", upper_count)
    print("No. of Lower case characters:", lower_count)

count_upper_lower("MY NAME is Taher")

#Q3

class PairFinder:
    def __init__(self, numbers, target):
        self.numbers = numbers
        self.target = target
    
    def find_pairs(self):
        pairs = []
        for i in range(len(self.numbers)):
            for j in range(i+1, len(self.numbers)):
                if self.numbers[i] + self.numbers[j] == self.target:
                    pairs.append((i, j))
        return pairs

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, -1]
target = 8
pf = PairFinder(numbers, target)
print(pf.find_pairs())


#Q4

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
print(is_prime(888))

#Q5

def ispalindrome(string):
    string = string.lower()
    string = ''.join(char for char in string if char.isalnum())
    return string == string[::-1]
print(ispalindrome("taher"))

#Q6
import string

def is_pangram(sentence):
    alphabet = set(sentence.lower())
    alphabet.discard(' ')
    return alphabet == set(string.ascii_lowercase)

print(is_pangram("The quick brown fox jumps over the lazy dog"))
