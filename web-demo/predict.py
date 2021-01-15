from pyvi import ViTokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.preprocessing.text import Tokenizer
from keras.models import load_model
import joblib
import numpy as np

MAX_SEQ_LENGTH = 100
LABELS = ['Phim / Nhạc / Sách', 'Điện thoại di động', '4 bánh', 'Đồ điện tử & Thiết bị gia dụng']

#Load trained objects
model = load_model('model.h5')
word_tokenizer = joblib.load("word_tokenizer")

def predictLabel(text):
    embedding = get_embedding(text)
    probability_vector = model.predict(embedding)
    resultLabel = indexToLabel(np.argmax(probability_vector))
    return resultLabel, probability_vector

def get_embedding(text):
      text= ViTokenizer.tokenize(text).split(text)
      text = word_tokenizer.texts_to_sequences(text)
      text= pad_sequences(text, maxlen=MAX_SEQ_LENGTH, padding="pre", truncating="post")
      return text;

def indexToLabel(idx, labels=LABELS):
    return labels[idx]
if __name__ == "__main__":
    test = 'Điện thoại Iphone10 vừa ra mắt thật đẹp muốn mua mà không có tiền'
    resultLabel, probability_vector = predictLabel(test)
    print ("Probability vector is: ", probability_vector)
    print ("The best fit class: ", resultLabel)
