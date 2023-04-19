import random
import streamlit as st
from PIL import Image
from pytube import YouTube

def download_audio(url):
    yt = YouTube(url)
    stream = yt.streams.filter(only_audio=True).first()
    filename = stream.download()
    return filename

def guess_number():
    st.title("Guess the Number")
    number = random.randint(1, 10)
    guess = st.number_input("Guess a number between 1 and 10:", min_value=1, max_value=10)
    if guess is not None:
        if guess == number:
            st.success("🎉🎂🎈 Happy Birthday! 🎈🎂🎉 May all your dreams come true and may this year bring you lots of joy, happiness and success. Enjoy your special day! 🎁🥳")
            balloons_img = Image.open("balloons.jpg")
            st.image(balloons_img, caption="Balloons!", use_column_width=True)
            st.write("Check out my personalized website at http://www.mywebsite.com")
            url = "https://www.youtube.com/watch?v=n3qw7lZzbkM" # replace with your own YouTube URL
            filename = download_audio(url)
            st.audio(filename, format="audio/mp3")
        else:
            st.warning("Wrong! Guess again.")

guess_number()
