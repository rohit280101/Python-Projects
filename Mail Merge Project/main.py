#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as files:
    names= files.readlines()


with open("./Input/Letters/starting_letter.txt")  as data:
    x = data.read()
    for i in names:
        stripped_letter =i.strip()
        letter = x.replace(PLACEHOLDER,stripped_letter)

        with open(f"./Output/ReadyToSend/{stripped_letter}.txt", mode="w") as data:
            data.write(letter)