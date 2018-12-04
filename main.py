import nltk
import os 

# Clear the screen
os.system("cls")

# Open the .txt file holding the text that will be edited and save it in before_text
with open("before.txt", "r") as f:
    before_text = f.read()

# Parse the sentences using nltk
sentences = nltk.sent_tokenize(before_text)

#Create an array to hold the editor's updates
after_text = []

# Loop through each sentence from before_text and have the editor input any revision, or they can simply enter skip to keep the sentnece as is
for i in sentences:
    print(i + "\n")
    editor_input = input("")
    if editor_input != "skip":
        after_text.append(editor_input)
    os.system("cls")

# Print the before and after versions
os.system("cls")
str_formating = ""
for i in after_text:
    str_formating = str_formating + i + " "
after_text = str_formating
print(before_text + "\n\n" + after_text)

# Write the after_text to the after.txt file
with open("after.txt", "w") as f:
    f.write(after_text)