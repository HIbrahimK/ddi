import re, os, time, pickle
import Util
from spell_correction import correction
from pathlib import Path
from turkishnlp import detector
from deasciifier import Deasciifier

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

def TurkceKontrol(text):
	delete_list = [",", "’"]
	tweet = Util.delete_characters_space(text, delete_list)
	word_list = tweet.split()
	word_list = [correction.correction(word) for word in word_list ]
	word_list = [word for word in word_list if len(word) > 1]
	word_list = Util.remove_words(word_list, stopwords)

	sentence = ""
	for word in word_list:
		sentence = sentence + " " + word

	return(sentence)
delete_list = [",", "’"]
#yöntem 1 iyi çalışmıyor
#print("sadece kökler : " , preprocess("deneme metin buraya yazilacak ekini kökünü bulmaca. Uzun bir metin ile denemeler, yapılabilir mi?"))
#print(Util.delete_characters("Makale, herhangi bir konuda, bir görüşü, bir düşünceyi savunmak ve kanıtlamak için yazılan yazılara denir. Gazete ve dergilerde yayımlanır. Bir gerçeği açıklamak, bir konuda görüş ve düşünceler öne sürmek ya da bir tezi savunmak, desteklemek için yazılan yazılara da ""makale"" denir.",delete_list))
print("Kelimenin en düzgün hali", correction.correction("Yüzelli"))
print("Kelimenin olası halleri", correction.candidates("Yüzelli"))

# print("Kelimenin olası halleri", correction.edits1("Türkcesi"))
# print("Kelimenin olası halleri", correction.edits2("Türkcesi"))
ornekMetin="Bugun dunya kadinlar gunu. Yuzelli yil once calisan kadinlarin daha iyi çalşıma kosullari ve erkeklerle esit haklar elde etmek icin ABD'de baslattiklari, 19. yuzyilin baslarinda Avrupa'ya da yayilan kadin hareketinin anisina kutlanan gun."
print(TurkceKontrol(ornekMetin))
#Yontem 2

obj = detector.TurkishNLP()
#obj.download()
obj.create_word_set()
print(obj.is_turkish("Yüzelli Ben bugün ankaraya gideceğim belki birşeyler alırım"))
lwords = obj.list_words("vri kumsi idrae edre ancaka daha güezl oalbılır")
print(obj.auto_correct(lwords))

lwords = "Yuzelli vri kümsi idrae edre ancaka daha güezl oalbılır"
deasciifier = Deasciifier(lwords)
my_deasciified_turkish_txt = deasciifier.convert_to_turkish()
lwords = obj.list_words(my_deasciified_turkish_txt)

print(obj.auto_correct(lwords))


lwords = obj.list_words(ornekMetin)
print(obj.auto_correct(lwords))

my_ascii_turkish_txt = ornekMetin
deasciifier = Deasciifier(my_ascii_turkish_txt)
my_deasciified_turkish_txt = deasciifier.convert_to_turkish()
print(my_deasciified_turkish_txt)
lwords = obj.list_words(my_deasciified_turkish_txt)
print(obj.auto_correct(lwords))
print(TurkceKontrol(my_deasciified_turkish_txt))

