# This script receives a string and determines if it is a palindrome
# Returns a boolean value
# The string can be anything, number, letters, symbols, as the script does not care
# Usage: isPalindrome.py <string>
# isPalindrome.py <string> "DEBUG" for extra debugging information

import sys
import logging

def isPalindrome(choc, *lawgs):
    log = logging.getLogger("isPalindrome")
    # If the caller has requested logs, give them logs!
    if("DEBUG" in lawgs):
        log.setLevel(logging.DEBUG)
        stdHandler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(logging.BASIC_FORMAT)
        stdHandler.setFormatter(formatter)
        log.addHandler(stdHandler)
        log.debug("Logs are ready")

    log.debug("String to check: \"" + choc + "\"")
    
    # Check if the caller passed in anything worthwhile
    if(len(choc) == 0):
        log.warning("The string is empty. Please enter a string")
        return False
    elif(len(choc) == 1):
        log.warning("The string has only one character. It is a palindrome")
        return True
    
    # This loop checks if the string is palindromic
    # It compares each end of the string until there is nothing left
    i = 0
    j = len(choc) - 1
    while(i < j):
        log.debug("Comparing character " + str(i) + ": " + choc[i] + " with character " + str(j) + ": " + choc[j])
        if(choc[i] == choc[j]):
            log.debug("MATCH")
            i += 1
            j -= 1
        else:
            log.debug("NO MATCH")
            log.warning(choc + " is not a palindrome")
            return False
    
    log.debug(choc + " is a palindrome")
    print(choc + " is a palindrome")
    return True

if(len(sys.argv) == 3 and sys.argv[2] == "DEBUG"):
    print(isPalindrome(sys.argv[1], 'DEBUG'))
elif(len(sys.argv) != 2):
    print("~~~~~~~~~~isPalindrome.py~~~~~~~~~~")
    print("This script receives a string and determines if it is a palindrome")
    print("The string can be anything, number, letters, symbols, as the script does not care")
    print("Usage: isPalindrome.py <string>")
    print("isPalindrome.py <string> \"DEBUG\" for extra debugging information")
else:
    print(isPalindrome(sys.argv[1]))