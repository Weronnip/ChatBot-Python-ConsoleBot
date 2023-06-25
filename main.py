import webbrowser
import subprocess
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
                    "4.calc\n"
                    "5.\n"
                    "6.\n"
                    "7.\n"
                    "8.\n"
                    "9.\n"
                    "10. stop\n")

    elif "youtube" in message:
        say_message("Opening YouTube\n")
        say_message("Please wait...\n")
        webbrowser.open('https://www.youtube.com/', new=1)
        say_message("Youtube has been successfully opened!\n")

    elif "author" in message:
        say_message("Author Bor: @Weronnip\n")

    elif "music" in message:
        say_message("Opening YandexMusic\n")
        say_message("Please wait...\n")
        webbrowser.open('https://music.yandex.ru/home?=', new=1)
        say_message("YandexMusic has been successfully opened!\n")

    elif "calc" in message:
        say_message("Opening calculator\n")
        say_message("Please wait...\n")
        subprocess.Popen('C:\\Windows\\System32\\calc.exe')
        say_message("Calculator has been successfully opened!\n")


    elif "stop" in message:
        say_message("Goodbye, My frend")
        exit()


    else:
        say_message("This command does not exist\n")

def say_message(message):
    print(message)

if __name__ == "__main__":
    while True:
        command = Starting()
        CommandBot(command)