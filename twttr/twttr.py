inp = input("Input: ")

isVowel = lambda x: x.lower() in ["a", "e", "i", "o", "u"]

out = ""

for i in inp:
    if not isVowel(i):
        out += i

print(out)