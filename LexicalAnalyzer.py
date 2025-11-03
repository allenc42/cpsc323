text = ""
with open("InputFile.txt") as f:
    #Going through the file line by line
    for line in f:
        #Get rid of all comments
        if "//" in line:
            start = line.find("//")
            #Deletes "//", and all characters afterwards
            line = line[:start]
        #Get rid of all whitespace
        line = line.replace(" ", "").strip()
        text += line

print(text)