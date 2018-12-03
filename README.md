# editor
This is a small little program to help facilitate the editing of short writing samples. 

# How to use this 
1) Paste the text that requires review into `before.txt`
2) Run `main.py`
3) The program will then go through the pasted text from `before.txt` sentence by sentence, asking for any edits
4) If you don't wish to make any edits to a sentence, simply just type in "skip"
5) Once all of the sentences have been reviewed, the program will then output the before and after versions on the screen
6) The final result is also saved to `after.txt`

# Todo 
1) Utilize with(open("filename", "filemode")) instead of var = open("filename", "filemode")
2) Find a better way to format the after_text for printing the final result
3) Instead of having the editor type skip, just let them press enter (no text needed to be entered)