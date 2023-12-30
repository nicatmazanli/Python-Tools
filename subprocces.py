import subprocess
import os
import time
from colorama import init, Fore, Back, Style
import urllib.request

try:


    def system():
        i = True
        while i:

            try:
                os.system("cls")
                os.system("clear")
                banner()
                ans = int(input(
                    "How you want to open the program \n    1 Give name \n    2 Path/exe \n    3 Get site "
                    "source-code\n    4 History(and hack simulator)\n        ?> "))
                os.system("cls")

                if ans == 1:
                    banner()
                    app_name = input("Please...Enter the app name :: ")
                    print("Well...Your app is opening...")
                    history(app_name)
                    os.system(app_name)

                elif ans == 2:
                    try:
                        banner()
                        app_path = input("Please...Enter the app path/name.exe ::> ")
                        print("Well...Your app is opening...")
                        history(app_path)
                        subprocess.call(app_path)
                    except OSError:
                        print("UH..OH..there are some problems to run this program...Please try another...")
                        input()

                elif ans == 3:
                    try:
                        ans = int(input("Please...Enter the web site link http/https ::>(1 | 2) "))

                        print()
                        if ans == 1:
                            url = input("Please...Enter the url ::> ")
                            urlls = str(urllib.request.urlopen("http://" + url).read())
                            history(url)
                            file = open("" + url + ".txt", "w+")
                            file.write(urlls)
                            print("File created and now opening ")
                            os.system("notepad " + url + ".txt ")

                        if ans == 2:
                            url = input("Please...Enter the url ::> ")
                            urlls = str(urllib.request.urlopen("https://" + url).read())
                            history(url)
                            file = open("" + url + ".html", "w+")
                            file.write(urlls)
                            print("File created and now opening ")
                            os.system("notepad " + url + ".html")
                    except urllib.error.HTTPError:
                        print("This link is invalid please try another link...")
                        input()
                    except urllib.error.URLError:
                        print("This link is invalid please try another link...")
                        input()

                elif ans == 4:
                    cls_hist()
            except ValueError:
                print()
                print("Please Enter correct value...")
                input()


    def hack():
        for i in range(10, 100000):
            s = i // 10 * " "

            # time.sleep()
            if i % 10 == 0:
                print(
                    Fore.GREEN + "" + s + " You are" + Style.BRIGHT + Fore.RED + " HACKED" + Fore.GREEN + " You are" + Style.BRIGHT + Fore.RED + " STUPIT" + Fore.GREEN + " You are" + Style.BRIGHT + Fore.RED + " NOTHING..." + Fore.YELLOW + "I AM Clever!! I AM hacker!!! I am coder!!!! I am your end!!!")

                os.system("clear")

                os.system("cls")


    init(autoreset=True)


    def history(app):
        history = open("hist.txt", "a")
        history.write(app + "\n")
        history.close()


    def cls_hist():
        os.system("cls")
        os.system("clear")
        print("<========== History ==========>")
        t = open("hist.txt", "r")
        hist = t.read()
        print(hist)
        t.close()
        clear = input("Clear history ?> (y/N/hack simulato === h) ")

        if clear == "y" or "Y":
            hist = open("hist.txt", "w")
            hist.close()
        if clear == "H" or "h":
            hack()


    def another_app(name):

        ans2 = input(
            "Do you want to open any another app or do you want to see history or do you want to see hack code ?> (Y/n/h/another key) ")
        if ans2 == "Y" or ans2 == "y":
            os.system("cls")
            os.system("clear")

            system()
        elif ans2 == "N" or ans2 == "n":
            os.system("cls")
            os.system("clear")

            print("OK... GOODBYE " + name.capitalize() + "!!!\n See you later...")
            quit()
        elif ans2 == "h" or ans2 == "H":
            cls_hist()
        else:
            hack()


    def banner():
        print(" /---------------------------------------------------------------\\")
        print("|The application does not open or url is not response ,           |\n" +
              "|you typed the name incorrectly or the path or link is incorrect  |")
        print(" \\---------------------------------------------------------------/\n\n")


    os.system("cls")  # for linux os.system("clear")
    print("Hello...")
    print("My name is Prime...")
    name = input("What is your name ?> ")
    print("Hmm...", name.capitalize() + "...")
    time.sleep(4)
    system()

except KeyboardInterrupt:
    another_app(name="Killer :(")
