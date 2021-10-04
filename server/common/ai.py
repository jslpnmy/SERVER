import tensorflow as tf
from konlpy.tag import Okt
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import json

model = tf.keras.models.load_model('C:\projects\hackathon\server\common\my_model.h5') #주소는 본인 파일 위치에 맞춰 바꿀 것
okt = Okt()
with open('C:/projects/hackathon/server/common/tokenizer.json') as f: #주소는 본인 파일 위치에 맞춰 바꿀 것
    data = json.load(f)
    tokenizer = tf.keras.preprocessing.text.tokenizer_from_json(data)

stopwords = ['은','는','이','가','을','를','으로','로','과','와','의','에','들','좀','도','한','하다']

def sentiment_predict(new_sentence):
  new_sentence = okt.morphs(new_sentence, stem=True)
  new_sentence = [word for word in new_sentence if not word in stopwords]
  encoded = tokenizer.texts_to_sequences([new_sentence])
  pad_new = pad_sequences(encoded, maxlen = 30)
  score = float(model.predict(pad_new))

  return (1-score)*100
