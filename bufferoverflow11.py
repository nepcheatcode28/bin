BUFFER_SIZE = 8
print("=== Buffer Overflow Lab ===")
data = input("Enter normal or oversized input: ")
print("Input received:", data)
print("Input length:", len(data))
if len(data) > BUFFER_SIZE:
print("\n[ALERT] Buffer Overflow Attempt Detected!")
print("Input exceeds the buffer limit.")
else:
print("\n[INFO] Input is within the limit.")
