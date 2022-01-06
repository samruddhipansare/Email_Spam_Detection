import pickle 
import streamlit as st 
from win32com.client import Dispatch

def speak(text):
	speak=Dispatch(("SAPI.SpVoice"))
	speak.Speak(text)

model=pickle.load(open("spam.pkl", "rb"))
cv=pickle.load(open("vectorizer.pkl","rb"))


def main():
	st.title("Email spam Classification Apps")
	st.subheader("Build With Streamlit & Python")
	msg=st.text_input("Enter a text:")
	if st.button("Predict"):
		data=[msg]
		vect=cv.transform(data).toarray()
		prediction=model.predict(vect)
		result=prediction[0]
		if result==1:
			st.error("This is a spam mail")
			speak("This is a spam mail")
		else:
			st.success("This is a ham mail")
			speak("This is a ham mail")
main()