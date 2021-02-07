Alphabet Soup Assessment

Everyone loves alphabet soup. And of course, you want to know if you can construct a message from the letters found in your bowl. 

Your Task: 

Write a function that takes as input two strings:

1- the message you want to write
2- all the letters found in your bowl of alphabet soup.

Assumptions:
- It may be a very large bowl of soup containing many letters.
- There is no guarantee that each letter occurs a similar number of times - indeed some letters might be missing entirely.
- The letters are ordered randomly.

The function should determine if you can write your message with the letters found in your bowl of soup. The function should return True or False accordingly. Try to make your function efficient.  Please use Big-O notation to explain how long it takes your function to run in terms of the length of your message (m) and the number of letters in your bowl of soup (s). You may write the function in any programming language you prefer - but please consider the language required by the position for which you are applying.
 
. 

Logic:

Converting the message into a list for easily iterate
Converting the alphabet string from the bowl into a list for easily iterate

Itrating the message list and chcking each character of the message if is included to the list of alphabet string
If it's included then removing the current character from the alphabet string, otherwise break the loop and return False

This Algorithm is pretty fast in concluding any lenght for the Alphabet string taken from the bowl of soup. This is 
simply because there is loop over the entire Alphabet soup but rather, over the letters of message. 
This cuts the execution time but half assuming we have thousand of words in the soup against very shourt message.
With a complexity of O(n) where "n" is the lenght of the message,  the execution time is very low, round 2.535e-05

First, clone the repository to your local machine:

```bash
git clone https://github.com/guido-lab/alphabet-soup.git
```

Create virtual enviroment:

```bash
python -m venv env
```

Activate enviroment:

```bash
source env/bin/activate
```

Install the requirements:

```bash
pip install -r requirements.txt
```

Finally, run the app:

```bash
python alphabetSoup.py
```

