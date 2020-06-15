import re, os, time, pickle
import Util
from spell_correction import correction
from pathlib import Path

src_folder = Path("./")
#stopwords = Util.read_file(Path(src_folder / "stopwords")).split("\n")
stopwords = []
#exclude = [".", ",", ":", ";", "?", "!", "\"", "#", "$", "%", "&", "\'", "\(", "\)", "\*", "+", "-", "\\", "/", "<", ">", "=", "@", "[", "]", "\^", "_", "`", "{", "}", "|", "~"]

"""
Preprocessing for training data
"""
def preprocess(text):
	delete_list = [",", "’"]
	tweet = Util.delete_characters_space(text, delete_list)
	word_list = tweet.split()
	word_list = [ Util.stem_word(correction.correction(Util.remove_punct(Util.remove_repeating_char(Util.remove_with_regex(word))))) for word in word_list ]
	word_list = [word for word in word_list if len(word) > 1]
	word_list = Util.remove_words(word_list, stopwords)

	sentence = ""
	for word in word_list:
		sentence = sentence + " " + word

	return(sentence)
"""
Creates tuples as (sentence, tag) and returns the list of the tuples
"""
print("sadece kökler : " , preprocess("deneme metin buraya yazilacak ekini kökünü bulmaca. Uzun bir metin ile denemeler, yapılabilir mi?"))
print("Kelimenin en düzgün hali", correction.correction("anahtrlık"))
print("Kelimenin olası halleri", correction.candidates("arba"))