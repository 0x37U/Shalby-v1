import os,sys
os.system("cls" or "clear")
print("""

 ██████╗ ██╗  ██╗██████╗ ███████╗██╗   ██╗
██╔═████╗╚██╗██╔╝╚════██╗╚════██║██║   ██║
██║██╔██║ ╚███╔╝  █████╔╝    ██╔╝██║   ██║
████╔╝██║ ██╔██╗  ╚═══██╗   ██╔╝ ██║   ██║
╚██████╔╝██╔╝ ██╗██████╔╝   ██║  ╚██████╔╝
 ╚═════╝ ╚═╝  ╚═╝╚═════╝    ╚═╝   ╚═════╝ 
        Github : github.com/0x37U
            FB : Priv8 Ghost
                SHALBY ♥
""")
choice = int(input("[1] information Generator\n[2] Bin Checker\n[3] Exit\nSELECT >").strip())

if choice == 1:
        os.system("Tools\info.py")
elif choice == 2:
        os.system("Tools\\bin.py")
elif choice == 3:
        sys.exit()