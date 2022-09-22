while True:
    command = input("> ")
    if command == 'exit':
        break
    print("Your command was: ", command)

while (command := input("> ")) != "exit":
    print("Your command aws: ", command)
