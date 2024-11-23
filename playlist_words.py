import streamlit as st
import random

words = ['bacon', 'cheese', "choc", "curry", "wowser"]

def give_output(encrypted = None):
    if encrypted[0] is not None:
        for num in encrypted:
            words.pop(deencrypt(int(num)))
    word = random.choice(words)
    index = words.index(word)
    code = encrypt(index)
    return (f"{word}, {code}", (word, code))


def encrypt(num):
    num = num * 2
    num += 474
    num = num * 2
    num -= 250
    return num

def deencrypt(num):
    num += 250
    num = int(num/2)
    num -= 474
    num = int(num/(2))  
    return num

words_string = ""
for word in words:
    words_string =  words_string + word + ", "


number = st.radio(
    "How many codes",
    ["1", "2", "3", "4"],
)

if number == "1":
    code = st.number_input("Insert a number", value=None,)
    if st.button("Give me my word"):
        output = give_output([code])
        st.write(output[0])
        st.write(words)
elif number == "2":
    code1 = st.number_input("Insert a number", value=None,)
    code2 = st.number_input("Insert a number", value=None, key = 2)
    code = (code1, code2)
    if st.button("Give me my word"):
        output = give_output(code)
        st.write(output[0])
    
elif number == "3":
    code1 = st.number_input("Insert a number", value=None,)
    code2 = st.number_input("Insert a number", value=None,  key = 2)
    code3 = st.number_input("Insert a number", value=None,  key = 3)
    code = (code1, code2, code3)
    if st.button("Give me my word"):
        output = give_output(code)
        st.write(output[0])

elif number == "4":
    code1 = st.number_input("Insert a number", value=None,)
    code2 = st.number_input("Insert a number", value=None,  key = 2)
    code3 = st.number_input("Insert a number", value=None,  key = 3)
    code4 = st.number_input("Insert a number", value=None,  key = 4)
    code = (code1, code2, code3, code4)
    if st.button("Give me my word"):
        output = give_output(code)
        st.write(output[0])

else:
    if st.button("Give me my word"):
        output = give_output()
        st.write(output[0])

st.write(words_string)


