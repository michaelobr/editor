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
1) Find a better way to format the after_text for printing the final result

# Important notes
This program performs tokenization utilizing the nltk module. To get the nltk module, simply run `pip install nltk` inside of command line. To setup tokenization, run the following inside python.
```
import nltk
nltk.download("punkt") 
```