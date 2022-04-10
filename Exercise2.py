str = input()

while True:

    command_input = input().split(" ")
    command = command_input[0]

    if command == "Done":
        break

    if command == "TakeOdd":
        str = str[1::2]
        print(str)

    elif command == "Cut":
        index = int(command_input[1])
        length = int(command_input[2])
        end = str[index:]
        final = end[length:]
        str = str[:index] + final
        print(str)
    elif command == "Substitute":
        substring = command_input[1]
        substitute = command_input[2]
        if substring in str:
            str = str.replace(substring, substitute)
            print(str)
        else:
            print("Nothing to replace!")

print(f"Your password is: {str}")