import deepnlp
deepnlp.download('ner')

from deepnlp import segmenter
from deepnlp import ner_tagger

tokenizer = segmenter.load_model(name = 'zh')
tagger    = ner_tagger.load_model(name = 'zh')

file_r = open('./data/person_resume.txt', 'r')
file_w = open('./data/person_resume02.txt', 'w')

for line in file_r:
    text = line.rstrip()
    words = tokenizer.seg(text)
    tagging = tagger.predict(words)
    for (w, t) in tagging:
        pair = w + ' ' + t
        file_w.write(pair)

file_w.close()
file_r.close()
