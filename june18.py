#type validation
value = input("Enter a number")

if value.isdigit():
    num = int(value)
    print(f"Converted to integer: {num}")

elif '.' in values:
    num = float(value)
    print(f"Converted to float :{num}")

else:
    print("Invalid number input")



