import pytesseract
from pdf2image import convert_from_path
from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route("/upload", methods=['POST'])
def upload():
  file = request.files['file']
  # this file can be image or pdf
  file.save(file.filename)
  text = ''
  if file.filename.endswith('.pdf'):
    images = convert_from_path(file.filename)
    for image in images:
      text += pytesseract.image_to_string(image, lang='eng+vie')
  else:
    text = pytesseract.image_to_string(file.filename, lang='eng+vie')
    
  # remove file after reading
  os.remove(file.filename)
  return render_template('index.html', text=text)

if __name__ == '__main__':
  app.run(debug=True)
