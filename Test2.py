from turkish_nlp import detector


obj = detector.TurkishNLP()
obj.create_word_set()
print(obj.is_turkish("Yüzelli Ben bugün ankaraya gideceğim belki birşeyler alırım"))
lwords = obj.list_words("vri kümsi idrae edre ancaka daha güezl oalbilir ")

print("1.: ",obj.auto_correct(lwords))

print("2. :",obj.get_candidate(lwords[7])) # Tek Kelime için Olası kelime önerilerinin ilk 5'ini  alır

"""
Elde ettiğimiz sonuç 
1.:  ['veri', 'kümesi', 'idare', 'eder', 'ancak', 'daha', 'güzel', 'olabilir']
2. : ['olabilir', 'oabilir', 'olbilir']
"""

