"""
Spell correction for Turkish words
Taken from:
    https://norvig.com/spell-correct.html
"""
import re, os
from collections import Counter
from pathlib import Path

WORDS = dict()

spell_folder = Path("./spell_correction")

def words(text): return re.findall(r'\w+', text.lower())
with open(os.path.expanduser(Path(spell_folder / "big2.txt")), "r", encoding = 'utf-8') as f:
    for line in f:
        splitted = line.split()
        WORDS[splitted[0]] = int(splitted[1])
#WORDS = Counter(words(open('big.txt').read()))

def P(word, N=sum(WORDS.values())):
    "Probability of `word`."
    if  word in WORDS.keys():
        number = WORDS[word]
    else:
        number = 1
    if number == 0:
        number = 1
    return number / N

def correction(word):
    "Most probable spelling correction for word."
    return max(candidates(word), key=P)

def candidates(word):
    "Generate possible spelling corrections for word."
    return (known([word]) or known(edits1(word)) or known(edits2(word)) or [word])

def known(words):
    "The subset of `words` that appear in the dictionary of WORDS."
    return set(w for w in words if w in WORDS)

def edits1(word):
    "All edits that are one edit away from `word`."
    letters    = 'abcçdefgğhıijklmnoöprsştuüvyzw'
    splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)]
    deletes    = [L + R[1:]               for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
    replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters]
    inserts    = [L + c + R               for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)

def edits2(word):
    "All edits that are two edits away from `word`."
    return (e2 for e1 in edits1(word) for e2 in edits1(e1))
def print_diff(word, s):
    if not word == s:
        print(word + " --> " + s)
counter = 0