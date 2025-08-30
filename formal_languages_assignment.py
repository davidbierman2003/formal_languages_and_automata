#author: David Bierman
#course: CS 4110 Formal Languages & Automata
#Instructor: Yong Zhang
#Written in python. To run it run in a termial while in the files current directory:  python formal_languages_assignment.py


#Task 1: Language Membership Testing (25 points)
#Implement a function that determines if a string belongs to the language:
#L = {a^nb^n | n> = 1} over alphabet {a, b}
#This language contains strings where:

#The number of 'a's equals the number of 'b's
#All 'a's come before all 'b's
#This is at least one 'a' and one 'b'.

def is_in_language_L(string):
    """
    Check if a string belongs to language L = {a^n b^n | n >= 1}
    Args:
        string (str): Input string to check
    
    Returns:
        bool: True if string is in L, False otherwise

    Examples:
        is_in_language_L("ab") -> true
        is_in_language_L("aabb") -> true
        is_in_language_L("aaabbb") -> true
        is_in_language_L("aba") -> False
        is_in_language_L("") -> False


        #pseudocode
        1. Test to see if the length of the in math: length(string) > 0
        if length(string) > 0 then the string might be part of this language. If it isn't greater than 0 return false.
    
        2. Look at the characters in the string. If the first character isn't an a return false.
        3. Count the number of 'a's in the string. Then count the number of 'b's in the string.
        4. If all the first characters are 'a's and the next characters are 'b's
         and the number of 'a's in the string is equal to the number of 'b's in the string return true.
         Otherwise return false.
    """
    #Test 1. Length test
    if( len(string) == 0 ):
        return False
    
    #Tests 2 and 3 listed above
    #The below code makes sure the first letter is 'a'
    #If the first character is not 'a' or 'b' then it will return false.
    #If the first character is 'b' it will return false because a_counter is 0.
    #If the first character is 'a' it will increase a_counter.
    #This will only allow the first characters to be 'a's and after the 'a's the next characters need to be 'b's.
    a_counter = 0
    b_counter = 0
    for char in string:
        if char == 'a' and (b_counter == 0):
            a_counter += 1
        elif char == 'b' and (a_counter > 0):
            b_counter += 1
        else:
            return False
    
    #Test 4 make sure the number of 'a's is the same as the number of 'b's
    if (a_counter == b_counter):
        return True
    else:
        return False

if __name__ == "__main__":
   print("The value of is_in_language_L('ab') is", is_in_language_L('ab'))
   print("The value of is_in_language_L('aabb') is", is_in_language_L('aabb'))
   print("The value of is_in_language_L('aaabbb') is", is_in_language_L('aaabbb'))
   print("The value of is_in_language_L('aba') is", is_in_language_L('aba'))
   print("The value of is_in_language_L('') is", is_in_language_L(''))
   print("The value of is_in_language_L('ba') is", is_in_language_L('ba'))
   print("The value of is_in_language_L('aaabb') is", is_in_language_L('aaabb'))
   
