#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

listnama = []
nama = ""
with open("/Programming/Python/100 Days of Code/9. Mail Merge Project/Mail Merge Project Start/Input/Names/invited_names.txt") as file:
# with open("\Programming\Python\\100 Days of Code\9. Mail Merge Project/Mail Merge Project Start/Input/Names/invited_names.txt") as file:
    
    for char in file.read():
        if char == "\n":
            listnama.append(nama)
            nama = ""
        elif char.isalpha() or char.isspace() :
            nama += char
    listnama.append(nama)        


text = ""
with open("/Programming/Python/100 Days of Code/9. Mail Merge Project/Mail Merge Project Start/Input/letters/starting_letter.txt") as letter:
    
    for char in letter.read():
        text+=char


for eachnama in listnama:
    with open(f"/Programming/Python/100 Days of Code/9. Mail Merge Project/Mail Merge Project Start/Output/ReadyToSend/letter_for_{eachnama}.txt", mode = "w") as finallet:
        replacedtxt = text.replace("[name]",eachnama)
        finallet.write(replacedtxt)
        
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp