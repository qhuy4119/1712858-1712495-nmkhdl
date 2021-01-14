from pyvi import ViTokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.preprocessing.text import Tokenizer
from keras.models import load_model

MAX_SEQ_LENGTH = 100
LABELS = set(['Phim / Nhạc / Sách', 'Điện thoại di động', '4 bánh', 'Đồ điện tử & Thiết bị gia dụng'])

model = load_model('model.h5')
test='Điện thoại Iphone10 vừa ra mắt thật đẹp muốn mua mà không có tiền'

def embedding(text):
      text= ViTokenizer.tokenize(text).split(text)
      text = word_tokenizer.texts_to_sequences(text)
      text= pad_sequences(text, maxlen=MAX_SEQ_LENGTH, padding="pre", truncating="post")
      return text;

def numToLabel(num, labels=LABELS):
    for (index, value) in enumerate(labels):
        if index==num:
            return value;
    return data[data.keys()[0]];
test = embedding(test)
probability_vector = model.predict(test)
print ("Probability vector is: ", probability_vector)
print ("The best fit class: ", numToLabel(probability_vector.index(max(probability_vector))))
