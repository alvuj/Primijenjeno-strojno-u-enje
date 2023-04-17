numbers = []

while True:
    user_input = input("Unesite broj (ili 'Done' za kraj): ")
    if user_input == "Done":
        break
    try:
        number = float(user_input)
        numbers.append(number)
    except ValueError:
        print("Neispravan unos, molimo unesite broj.")

count = len(numbers)
average = sum(numbers) / count
minimum = min(numbers)
maximum = max(numbers)

print(f"Korisnik je unio {count} brojeva.")
print(f"Srednja vrijednost je {average:.2f}.")
print(f"Najmanja vrijednost je {minimum:.2f}.")
print(f"Najveća vrijednost je {maximum:.2f}.")

numbers.sort()
print("Sortirana lista:")
print(numbers)