from machinetranslation import translator 
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    translated = translator.english_to_french(textToTranslate)
    return translated
    

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    translated = translator.french_to_english(textToTranslate)
    return translated

@app.route("/")
def renderIndexPage():
    return render_template("index.html")
    
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)