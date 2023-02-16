import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)
#  Init is used to initialize the module.

print("\033[31m" + "some red text")  # (Fore.RED is storing the color code)
print("\033[39m")  # and reset to default color (it is a clear character)

print()
print(f"{Fore.RED}C{Fore.GREEN}O{Fore.YELLOW}L{Fore.BLUE}")
print(f"{Fore.RED}Red Text")
print(f"{Fore.GREEN}Green Text")
print(f"{Fore.YELLOW}Yellow Text")
print(f"{Fore.BLUE}Blue Text")
print(f"{Fore.MAGENTA}Magenta Text")
print(f"{Fore.CYAN}Cyan Text")
print(f"{Fore.WHITE}White Text")
print()
print(f"{Back.RED}C{Back.GREEN}O{Back.YELLOW}L{Back.BLUE}")
print(f"{Back.RED}Red Background")
print(f"{Back.GREEN}Green Background")
print(f"{Back.YELLOW}Yellow Background")
print(f"{Back.BLUE}Blue Background")
print(f"{Back.BLACK}Black Background")
print(f"{Back.MAGENTA}Magenta Background")
print(f"{Back.CYAN}Cyan Background")
print(f"{Back.WHITE}White Text")
print()
print(f"{Style.DIM}S{Style.NORMAL}T{Style.BRIGHT}Y{Style.RESET_ALL}")
print(f"{Style.DIM}Dim Text")
print(f"{Style.NORMAL}Normal Text")
print(f"{Style.BRIGHT}Bright Text")
print()


#  F strings
print(f"{Fore.RED} red")
