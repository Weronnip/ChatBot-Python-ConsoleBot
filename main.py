import webbrowser
def Starting():
     return input("Enter command: ")

def CommandBot(message):
    message = message.lower()

    if "start" in message:
        say_message("\nHello, Bro!")
        say_message(" ")
        say_message("List command:\n\n"
                    "1. youtube\n"
                    "2. author\n"
                    "3. music\n"
                    "4. stop\n")

    elif "youtube" in message:
        say_message("Opening YouTube\n")
        say_message("Please wait...\n")
        webbrowser.open('https://www.youtube.com/', new=1)
        say_message("Youtube has been successfully opened\n")

    elif "stop" in message:
        say_message("Goodbye, My frend")
        exit()


    else:
        say_message("This command does not exist")

def say_message(message):
    print(message)

if __name__ == "__main__":
    while True:
        command = Starting()
        CommandBot(command)