from turkish_nlp import detector
from deasciifier import Deasciifier

obj = detector.TurkishNLP()
obj.create_word_set()
print(obj.is_turkish("Yüzelli Ben bugün ankaraya gideceğim belki birşeyler alırım"))
lwords = obj.list_words("vri kümsi idrae edre ancaka daha güezl oalbilir ")

print("1.: ",obj.auto_correct(lwords))

print("2. :",obj.get_candidate(lwords[0])) # Tek Kelime için Olası kelime önerilerinin ilk 5'ini  alır

"""
Elde ettiğimiz sonuç 
1.:  ['veri', 'kümesi', 'idare', 'eder', 'ancak', 'daha', 'güzel', 'olabilir']
2. : ['olabilir', 'oabilir', 'olbilir']
"""

"""test2"""

ornekMetin = "Bugun dunya kadinlar gunu. Yuzelli yil once calisan kadinlarin daha iyi calisma kosullari ve erkeklerle esit haklar elde etmek icin ABD'de baslattiklari, 19. yuzyilin baslarinda Avrupa'ya da yayilan kadin hareketinin anisina kutlanan gun."
ornekMetin2 = "vri kümsi idrae edre ancaka daha güezl oalbilir "
lwords = obj.list_words(ornekMetin)
print("3.: ",obj.auto_correct(lwords))
print("5. :",obj.get_candidate(lwords[1]))
"""Ascii dönüşüm yapılırsa"""
deasciifier = Deasciifier(ornekMetin)
my_deasciified_turkish_txt = deasciifier.convert_to_turkish()
lwords = obj.list_words(my_deasciified_turkish_txt)

print("4.: ",obj.auto_correct(lwords))
print("5. :",obj.get_candidate(lwords[0]))