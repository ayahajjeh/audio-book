import pyttsx3
import PyPDF2
from tkinter.filedialog import *

book = askopenfilename()
pdfreader = PyPDF2.PdfReader(book)
pages = len(pdfreader.pages)

for num in range(0, pages):
    page = pdfreader.pages[num]
    text = page.extract_text()
    speaker = pyttsx3.init()
    speaker.say(text)
    speaker.runAndWait()