'''
The Program accepts any number of arguments and checks if the passwords given have ever been leaked.
'''
import requests
import hashlib
from sys import argv


def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    re = requests.get(url)
    if re.status_code != 200:
        raise RuntimeError(f'Error. Entered password should be hashed. {re.status_code}')
    return re

def get_pw_leaks_num(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for i, count in hashes:
        if i == hash_to_check:
            return count 
    return 0 

def pwned_api_check(password):
    sha1pw = hashlib.sha1(str(password).encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1pw[:5], sha1pw[5:]
    response = request_api_data(first5_char)
    return get_pw_leaks_num(response, tail)

def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f"{password} has been leaked {count} times. It's advised to change the password. ❌\n")
        else:
            print(f"{password} has never been leaked. ✅\n")
    return "Done."
    
if __name__ == '__main__':
    main(argv[1:])
