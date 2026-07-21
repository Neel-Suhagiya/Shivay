import argparse
import hashlib
from colorama import init ,Fore ,Style
import sys
import subprocess



init(autoreset=True)
ascii_banner2 = r""" 

      
                                          <'\   A   /'>
                                           \ \_[ ]_/ /
               ____  _     _                \__ . __/
              / ___|| |__ (_)_   ____ _ _   _  [ ]
              \___ \|  _ \| \ \ / / _` | | | | [ ]
               ___) | | | | |\ V / (_| | |_| | [ ]                     
              |____/|_| |_|_| \_/ \__,_|\__, | [ ]
                                        |___/  (.)   

                                             By Neel Suhagiya 
""" 

if __name__ == "__main__":

    parser=argparse.ArgumentParser(add_help=False, description="Supported Hashtype :- md5, sha1, sha256, sha512")

    parser.add_argument(
        "--help",
        action="help",
        help="[*] show this help message and exit" 
    )

    parser.add_argument(
        "--user",
        action='store_true',
        help="""[*] It will use user mode :-
         This mode is use for cracking a hash build with personal info
        """
    )

    parser.add_argument(
        "--wordlist",
        metavar="",
        help= "[*] Use the Wordlist ,that you want to use specific",
        default="rockyou.txt"
    )

    parser.add_argument(
        "--format",
        metavar="",
        help="[*] Specify your hash  format "
    )

    parser.add_argument(
        "--hash",
        metavar="",
        help="[*] If you have single hash, then use it"
    )

    parser.add_argument(
        "--all",
        action='store_true',
        help="[*] It will use all available wordlist"
    )

    parser.add_argument(
        "--file",
        metavar="",
        help="[*] If you have file of hash, then mention file with path"
    )

    parser.add_argument(
        "--output",
        metavar="",
        help="[*] Store the output in given file"
    )

    args=parser.parse_args()

# parsing value to string value

wordlist = str(args.wordlist)
format = str(args.format).lower()
hash = str(args.hash)
file = str(args.file)
output_file = str(args.output)

# flag variable indicate that particular hash cracked or not -- "0" means not cracked, "(x > 0)" means cracked.

flag = 0

# printing help menu


print(Fore.RED + Style.BRIGHT + ascii_banner2)
print(Fore.GREEN + Style.BRIGHT + "******************************  Help menu  ********************************")
print("\n")
subprocess.run(["python", "shivay.py", "--help"])
print("\n")

if(args.output):
    pass
else:
    print(Fore.GREEN + Style.BRIGHT + "*******************************  Result  **********************************")
print("\n")



# Hash idenifier function

def hash_Identifier(a):
    if(len(a)==32):
        return "md5"
    elif(len(a)==40):
        return "sha1"
    elif(len(a)==64):
        return "sha256"
    elif(len(a)==128):
        return "sha512"
    else:
        return
    


# Hash Cracking function


def crack_Hash(Hash_string ,type ,word_list):
    global flag
    if ( (type == "md5") or (type == "MD5") ):
        with open(word_list,"r", errors='ignore') as f:
            for i in f:
                word_byte=(i.strip()).encode()
                h = hashlib.md5(word_byte).hexdigest()
                if (Hash_string == h):
                    flag = flag + 1
                    if(args.output):
                        with open(output_file, "a") as f:
                            f.write(f"{h} --> {i}")      
                    else:
                        print(f"{Fore.YELLOW + Style.BRIGHT + h} --> {Fore.MAGENTA + Style.BRIGHT + i}")
                    break


    elif ( (type == "sha256") or (type == "SHA256") ):
        with open(word_list,"r", errors='ignore') as f:
            for i in f:
                word_byte=(i.strip()).encode()
                h = hashlib.sha256(word_byte).hexdigest()
                if (Hash_string == h):
                    flag = flag + 1
                    if(args.output):
                        with open(output_file, "a") as f:
                            f.write(f"{h} --> {i}")
                    else:
                        print(f"{Fore.YELLOW + Style.BRIGHT + h} --> {Fore.MAGENTA + Style.BRIGHT + i}")
                    break

    
    elif ( (type == "sha512") or (type == "SHA512") ):
        with open(word_list,"r", errors='ignore') as f:
            for i in f:
                word_byte=(i.strip()).encode()
                h = hashlib.sha512(word_byte).hexdigest()
                if (Hash_string == h):
                    flag = flag + 1
                    if(args.output):
                        with open(output_file, "a") as f:
                            f.write(f"{h} --> {i}")
                    else:
                        print(f"{Fore.YELLOW + Style.BRIGHT + h} --> {Fore.MAGENTA + Style.BRIGHT + i}")
                    break

    
    elif ( (type == "sha1") or (type == "SHA1")):
        with open(word_list,"r", errors='ignore') as f:
            for i in f:
                word_byte=(i.strip()).encode()
                h = hashlib.sha1(word_byte).hexdigest()
                if (Hash_string == h):
                    flag = flag + 1
                    if(args.output):
                        with open(output_file, "a") as f:
                            f.write(f"{h} --> {i}")
                    else:
                        print(f"{Fore.YELLOW + Style.BRIGHT + h} --> {Fore.MAGENTA + Style.BRIGHT + i}")
                    break



# It will use user mode
# User mode :- if it is know that the given hash is related to victim's personal info, then by provide the personal info of victim we can create millions of password and can able to crack uncrackable hashes.


if(args.user):
    try:
        flag=0
        print("\n")
        answer = input("Do you want to use, The final Weapon of Lord Shiv (yes / no) : ")
        print("\n")
    except(KeyboardInterrupt) as e:
        print("\n" + Fore.MAGENTA + Style.BRIGHT + "External interrupt occur..!")
        sys.exit()
   
    
    if( answer.lower() == "yes"):
        print('''
Description :
          
        If you are performing "Password cracking", then this feature is for you.
        During passowrd cracking it may be possible victim use Password formed by Combination of personal info,
        Like,
          shivam@1234 , shivam@<birth date of shivam>
        this feature will crack that type of password, which is very hard to crack by "Brute force method".
        For that, you have to provide victim's basic info.
        More info of victim means high number of chance to crack the password.
          ''')
        
        try:
            subprocess.run(["python", "user_data.py"])
            print("\n")
            crack_Hash(hash, format, r"wordlist\ user_data.txt")
            if(flag == 0):
                print(f"{Fore.YELLOW + Style.BRIGHT + hash}" + Fore.MAGENTA + Style.BRIGHT + " Not Cracked")
                print("\n")
        except(UnicodeDecodeError, SyntaxError) as e:
            print(Fore.MAGENTA + Style.BRIGHT + "Error has been occur..!")
            print("\n")
    else:
        print("Thank you for use this tool..!🙂")
        print("\n")
       
else:

    # Hash cracking using "hash" argument (single hash)
    
    try:
        if(args.hash):
    
            if(format in ["md5","sha512","sha256","sha1"]):
                print(f"{Fore.YELLOW + Style.BRIGHT + hash}" + " --> " + Fore.MAGENTA + Style.BRIGHT + "Hash type not suppored")
                print("\n")
            else:   
    
                if(args.all):
                    crack_Hash(hash , format , r"wordlist\Number.txt")
                    if(flag == 0):
                        crack_Hash(hash , format , r"wordlist\abcd.txt")
                    if(flag == 0):
                        crack_Hash(hash , format , r"wordlist\Number(4).txt")
                    if(flag == 0):
                        crack_Hash(hash , format , r"wordlist\Number(6).txt")
                    if(flag == 0):
                        crack_Hash(hash , format , r"wordlist\rockyou.txt")
                    if(flag == 0):
                        print(f"{Fore.YELLOW + Style.BRIGHT + hash}" + Fore.MAGENTA + Style.BRIGHT +" Not Cracked")
                        print("\n")
                else:
                    crack_Hash(hash , format , wordlist)
                    if(flag == 0):
                        print(f"{Fore.YELLOW + Style.BRIGHT + hash}" + Fore.MAGENTA + Style.BRIGHT + " Not Cracked")
                        print("\n")

    except(UnicodeDecodeError, SyntaxError, FileNotFoundError) as e:
        print(Fore.MAGENTA + Style.BRIGHT + "Error has been occur..!")
        print("\n")
    
        
    # Hash cracking of hash file ( Multiple different type of hash )
    
    try:
        if (args.file):
            with open(file,"r") as f1:
                for i in f1:
                    flag = 0
                    Hash = i.strip()
                    multiple_type = hash_Identifier(Hash)
                    
                    if(multiple_type == None):
                        print(f"{Fore.YELLOW + Style.BRIGHT + Hash}" + Fore.MAGENTA + Style.BRIGHT + " Hash type not suppored")
                        print("\n")
                        continue
                    else:
                        if(args.all):
                            crack_Hash(Hash , multiple_type , r"wordlist\Number.txt")
                            if(flag == 0):
                                crack_Hash(Hash , multiple_type , r"wordlist\abcd.txt")
                            if(flag == 0):
                                crack_Hash(Hash , multiple_type , r"wordlist\Number(4).txt")
                            if(flag == 0):
                                crack_Hash(Hash , multiple_type , r"wordlist\Number(6).txt")
                            if(flag == 0):
                                crack_Hash(Hash , multiple_type , r"wordlist\rockyou.txt")
                            if(flag == 0):
                                print(f"{Fore.YELLOW + Style.BRIGHT + Hash}" + Fore.MAGENTA + Style.BRIGHT + " Not Cracked")
                                print("\n")
                        else:
                            crack_Hash(Hash , multiple_type , wordlist)
                            if(flag == 0):
                               print(f"{Fore.YELLOW + Style.BRIGHT + Hash}" + Fore.MAGENTA + Style.BRIGHT + " Not Cracked")
                               print("\n")
                                     
    except(UnicodeDecodeError, SyntaxError, FileNotFoundError) as e:
        print(Fore.MAGENTA + Style.BRIGHT + "Error has been occur..!")
        print("\n")
    
    
# Show the msg that file password is cracked and stored in file


if(args.output and flag>0):
    print("Cracked password stored in given file..!👍")
    print("\n")



        




