# Shivay - The Hash Cracker

Shivay is a one type of dictionary-based hash cracking tool also use for Password Cracking purpose. It is develope for to crack hash in fast and efficient way. Conventional method like brute force is very time and energy consuming. So, mitigate that problem to develop a dictionary-based tool is a best option. Because, it is only target potential passwords. It is demonstrates, how dictionary attacks work against hashed passwords by generating and testing different types of wordlists.


# Screenshot

<img src="Images\Screenshot.png" width="1000" height="700">
You can also provide the text file with hash strings
<br></br>
<img src="Images\Screenshot-2.png" width="1000" height="700">


# Installation

For install tool use this git command.

      git clone https://github.com/Neel-Suhagiya/Shivay.git


# Using shivay

* for help menu use `--help` key.

      python shivay.py --help

* To specify the wordlist explicitly, use `--wordlist <wordlist_name>`. `rockyou.txt` is a default wordlist.

      python shivay.py --hash 81dc9bdb52d04dc20036dbd8313ed055 --format md5 --wordlist wordlist\abcd.txt

* Use `--all` key for to use all wordlist.

      python shivay.py --hash 81dc9bdb52d04dc20036dbd8313ed055 --format md5 --all

* To specify the type of the hash use `--format` key.

* For provide hash to the tool there is two way

  By using `--hash` key

      python shivay.py --hash 81dc9bdb52d04dc20036dbd8313ed055 --format md5

  By using `--file <file_name>`. provide the file that contain the list of hashes, tool will automatically recognize type of hash in the file.

      python shivay.py --file hash.txt --wordlist wordlist\abcd.txt

* For store the output in the file, use `--output <file_name>` key.

      python shivay.py --hash 81dc9bdb52d04dc20036dbd8313ed055 --format md5 --wordlist wordlist\abcd.txt --output result.txt




