# Prompt the user for a greeting
greeting = input("Greeting: ")

# Clean the greeting: remove leading whitespace and make it lowercase
clean_greeting = greeting.strip().lower()

# Check the conditions
if clean_greeting.startswith("hello"):
    print("$0")
elif clean_greeting.startswith("h"):
    print("$20")
else:
    print("$100")
