from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench/<textToTranslate>")
def englishToFrench(textToTranslate):
    # Write your code here
    text = translator.englishtofrench(textToTranslate)
    return text

@app.route("/frenchToEnglish/<textToTranslate>")
def frenchToEnglish(textToTranslate):
    
    # Write your code here
    text = translator.frenchtoenglish(textToTranslate)
    return text

@app.route("/")
def renderIndexPage():
    render_template("/templates/index.html")
    pass

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
