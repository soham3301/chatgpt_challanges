import time

# Print the message (end="" prevents jumping to a new line)
print("This message will disappear in 3 seconds...", end="", flush=True)

# Pause the program for 3 seconds
time.sleep(3)

# Overwrite the text with blank spaces to "delete" it
print("\r" + " " * 50 + "\r", end="", flush=True)

print("Done!")
