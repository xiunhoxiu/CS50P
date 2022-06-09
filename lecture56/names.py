names = []

for _ in range(3):
    names.append(input("what is your name? "))

# sort list in a loop
for name in sorted(names):
    print(f"hello, {name}")
