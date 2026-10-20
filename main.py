

number = int(input("Provide starting number: "))
step = int(input("Provide step: "))

print(f"{number} - {step} = {number - step}")

for i in range(5):
    print(number)
    number += step    
