text = "" #The text file
holder = "" #Holder for adding to our output
output = "" #final output
stringHolder = False #If holder has a string or not

#Tokens
keywords = ["int", "if", "return", "float", "string", "char"]
operators = ["+", "-", "=", "<", ">"]
double_operators = ["==", "!=", ">=", "<="]
separators = ["(", ")", "{", "}", ";"]

with open("InputFile.txt") as f:
    #Going through the file line by line
    for line in f:
        #Get rid of all comments
        if "//" in line:
            start = line.find("//")
            line = line[:start] #Deletes "//", and all characters afterwards
        line = line.strip() #Get rid of unneeded whitespace
        text += line #text without unnecessary whitespaces or comments

#Goes through the string character by character
i = 0
while i < len(text):
    char = text[i] #our current character

    #If character starts with ' or ", we will get the entire string literal
    if char == "'" or char == '"':

        start_string = char #determining if its " or '
        holder = char

        #Checks the next character ahead to determine if there is a ' or "
        j = i + 1
        while j < len(text) and text[j] != start_string: #if it does not equal ' or ", we keep iterating until it does
            holder += text[j]
            j += 1

        #Gets the last " or ' of the string
        if j < len(text):
            holder += text[j]

        i=j #Update our current index 
        stringHolder = True #States that our holder is a string

    #Looks ahead by one to check if operator has two symbols
    if i + 1 < len(text):
        char_longer = text[i+1]
    
    #Check to see if our current character is not a whitespace, is currently not a string, operator, or separator 
    if char != " " and stringHolder == False and char not in operators and char not in separators:
        #Adds our character to a holder
        holder += char
    #If met with a whitespace, string, operator, or separator, add the token to output
    else:
        #if holder not empty, add to output
        if holder != "":
            if holder in keywords:
                output += f'"{holder}" = keyword '
            elif holder.isdigit():
                output += f'"{holder}" = integer '
            elif holder[0] == '"' or holder[0] == "'":
                output += f'"{holder}" = string literal '
                stringHolder = False
            else:
                output += f'"{holder}" = identifier '

        holder = "" #resets holder once added to output

        #Add the operator and separator to output
        if char in operators:
            #Checks to see if the operator consist of two characters(ie, ==, !=, >=, <=)
            if char + char_longer in double_operators:
                output += f'"{char + char_longer}" = operator '
                i += 2
                continue
            else:
                output += f'"{char}" = operator '

        if char in separators:
            output += f'"{char}" = separator '
    i += 1

print(output)