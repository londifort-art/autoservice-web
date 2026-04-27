from flask import Flask, render_template, redirect, request
import json

app = Flask(__name__)

SUPPORTED_LANGUAGES = ['ru', 'lv', 'en']

@app.route('/')
def index():
    # Redirect to default language (Russian)
    return redirect('/ru')

@app.route('/<lang>')
def home(lang):
    if lang not in SUPPORTED_LANGUAGES:
        return redirect('/ru')
    
    # Загружаем переводы каждый раз, чтобы не нужно было перезапускать сервер
    with open('translations.json', 'r', encoding='utf-8') as f:
        translations = json.load(f)
        
    t = translations.get(lang, translations['ru'])
    return render_template('index.html', t=t, lang=lang)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)
