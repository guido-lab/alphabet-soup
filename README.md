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
git clone https://github.com/guido-lab/kira.git
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