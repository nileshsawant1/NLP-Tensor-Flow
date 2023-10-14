import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer


input = input("Input->")

print (input)

if input=="1":
    sentenses = ['i love my dog','i love my cat']
    sentenses = ['i love my dog','i love my cat','you love my dog!']
    sentenses = ['i love my dog','i love my cat','you love my dog!','do you think my dog is amazing?']

    tokenizer = Tokenizer(num_words=100)
    tokenizer.fit_on_texts(sentenses)

    word_index = tokenizer.word_index
    print (word_index)

    sequences = tokenizer.texts_to_sequences(sentenses)
    print (sequences)
elif(input=="2"):
    sentenses = ['i love my dog','i love my cat','you love my dog!','do you think my dog is amazing?']

    tokenizer = Tokenizer(num_words=100,oov_token="<OOV>")
    tokenizer.fit_on_texts(sentenses)

    word_index = tokenizer.word_index
    print (word_index)

    sequences = tokenizer.texts_to_sequences(sentenses)

    test_data = ['i really love my dog','my dog loves my manatee']
    sequences = tokenizer.texts_to_sequences(test_data)

    print (sequences)

