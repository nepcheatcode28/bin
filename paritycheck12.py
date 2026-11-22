data = input("Enter 4-bit data: ")
count = data.count("1")
if count % 2 == 0:
parity = "0" else:
parity = "1" print("Parity bit:", parity)
received = input("Enter received data with parity bit: ")
if received.count("1") % 2 == 0:
print("No error detected")
else:
print("Error detected!")