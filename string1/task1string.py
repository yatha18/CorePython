s= "This is string example."

#Reverse the complete string
result = s[::-1]

print("Reverse:", result)

#Word-wise reverse
s = "this is string example"
words = s.split()
words = words[::-1]
result = " ".join(words)

print("\nWord-wise reverse:", result)

#INTERCHANGE 2 CARACTERS
s = "this is string example"
result = ""

for i in range(0, len(s), 2):
    result = result + s[i:i+2][::-1]

print("\n2 characters interchange:", result)

#Split by space and join with *

s = "this is string example"

words = s.split(" ")
result = "*".join(words)

print("\nAfter split and join:", result)



#Replace is with was
s = "this is string example"

words = s.split()

for i in range(len(words)):
    if words[i] == "is":
        words[i] = "was"

result = " ".join(words)

print("\nAfter replacing 'is' with 'was':", result)
