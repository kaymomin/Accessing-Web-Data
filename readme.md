# ACCESSING WEB DATA USING PYTHON

## Quick Guide: Regular Expressions 
![RegexQuick](https://user-images.githubusercontent.com/44579545/66266852-189eef00-e844-11e9-8393-d488140b8812.JPG)
<br/>
Inside Python, regular expressions are sort of not built into the base language, like strings, lists or dictionaries. And so we have to import at the beginning with the import statement that says, pull in the regular expression library for the program. And there's a couple things you can play with. One is "re.search", which has the search capability from the regular expression library, and that tells you yes or no, did it work, and it's like a really smart find. And then "findall" is like an extraction. It's way more powerful than slicing, but it is the idea of finding the beginning and end of a bit of stuff, and pulling that out.
<br/>
## The Regex Module
Before you can use regular expression in your program, you must import the library using "import re". <br/>
You can use "re.search()" to see if a string matches a regular expression. You can use "re.findall()" to extract portion of the string that match your regular expression.
<br/>
### Using re.search() like find()
[Link to Code](Codes/searchfind.py)

### Using re.search() like startswith()
[Link to Code](Codes/searchStartswith.py)
