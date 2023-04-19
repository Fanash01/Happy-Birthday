import streamlit as st
import random
from PIL import Image

def guess_number():
    st.write("# Guess the number and get a birthday surprise!")
    st.write("Choose a number between 1 and 10:")
    number = st.number_input("", min_value=1, max_value=10, step=1, key="number_input")
    if st.button("Guess"):
        if random.randint(1, 3) == number:
            st.write("## 🎉 Congratulations! You guessed the correct number. 🎉")
            balloons_img = Image.open("balloons.jpg")
            st.image(balloons_img, use_column_width=True)
            
        else:
            st.write("Sorry, that's not the correct number. Try again!")
            
if __name__ == "__main__":
    guess_number()
