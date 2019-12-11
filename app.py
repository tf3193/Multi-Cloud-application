from flask import Flask, render_template, request
import langRequests
app = Flask(__name__)
app.debug = True


@app.route('/', methods=['GET'])
def dropdown():
    """Default path for the flask application. Displays index.html. 
    """
    languages = langRequests.lang_mapping.keys()
    return render_template('index.html', languages=languages)


@app.route('/Translate', methods=['GET', 'POST'])
def SomeFunction():
    """Function called from the button in index.html. It will create the Watson_translator class and then make an api call
    to IBM cloud. 
    
    Returns:
        [str] -- json-like string of translation, number of words and characters. 
    """
    output_lang = request.form.get('output_lang')
    input_lang = request.form.get('input_lang')
    api_key = request.form.get('api_key')
    url = request.form.get('api_end_point')
    input_text = request.form.get('name')
    translator = langRequests.Watson_Translator(
        api_key=api_key, input_text=input_text, input_lang=input_lang, output_lang=output_lang, url=url)
    print(translator.get_output_text)

    return str(translator.get_output_text())


if __name__ == "__main__":

    app.run(host='0.0.0.0')
