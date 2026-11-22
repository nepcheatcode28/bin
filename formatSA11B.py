user_input = input("Enter a message: ")
print("\nChecking user input...")
dangerous_patterns = ["%x", "%s", "%n", "%p"]
detected = False
for pattern in dangerous_patterns:
if pattern in user_input:
print("[ALERT] Suspicious format specifier:", pattern)
detected = True
if detected:
print("Potential format string attack detected!")
print("Displaying input safely:", user_input)
else:
print("No known format specifiers detected.")
print("Message:", user_input)