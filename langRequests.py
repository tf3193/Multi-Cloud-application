from requests.auth import HTTPBasicAuth
import requests
import json

lang_mapping = {'Afrikaans': "af", "Albanian": "sq", 'Arabic': "ar",
                "Armenian": "hy", 'Azerbaijani': "az", 'Bashkir': "ba",
                "Basque": "eu", 'Belarusian': "be", 'Bulgarian': "bg",
                'Bengali': 'bn', 'Catalan': 'ca', "Central Khmer": "km",
                'Czech': 'cs', 'Chuvash': 'cv', 'Simplified Chinese': 'zh',
                "Traditional Chinese": "zh-TW", 'Croatian': 'hr',
                'Danish': 'da', 'Dutch': "nl", 'English': "en",
                "Esperanto": "eo", 'Estonian': "et", 'Finnish': "fi",
                'French': "fr", "Georgian": "ka", 'German': "de", 'Greek': "el",
                "Gujarati": "gu", "Haitian": "ht",  'Hebrew': "he", 'Hindi': "hi",
                'Hungarian': "hu", "Icelandic": "is", 'Italian': "it",
                'Irish': "ga", 'Japanese': "ja", 'Korean': "ko",
                "Kazakh": "kk", "Kurdish": "ku", "Kirghiz": "ky", 'Lithuanian': "lt",
                "Latvian": "lv", "Malayalam": "ml", "Mongolian": "mn", "Malay": "ms",
                "Maltese": "mt", 'Norwegian Bokmal': "nb", "Norwegian Nynorsk": "nn",
                "Panjabi": "pa", "Persian": "fa", 'Polish': "pl", 'Portuguese': "pt",
                "Pushto": "ps", 'Romanian': "ro", 'Russian': "ru", "Serbian": "sr",
                'Slovakian': "sk", 'Slovenian': "sl", "Somali": "so", 'Spanish': "es",
                'Swedish': "sv", "Tamil": "ta", "Telugu": "te", 'Thai': "th",
                'Turkish': "tr", "Ukrainian": "uk", "Urdu": "ur", "Vietnamese": "vi"}


class Watson_Translator:
    api_key = ""
    input_text = ""
    output_text = ""
    input_lang = ""
    output_lang = ""
    url = ""

    def __init__(self, api_key, input_text, input_lang, output_lang,  url):
        """Constructor for the class. 
        
        Arguments:
            api_key {[str]} -- the end user API key
            input_text {[str]} -- input text to be translated
            input_lang {[str]} -- language of input_text
            output_lang {[str]} -- language for input_text to be translated to. 
            url {[str]} -- endpoint for watson_translator
        """
        self.api_key = api_key
        self.input_lang = input_lang
        self.input_text = input_text
        self.output_lang = output_lang
        self.url = url

    def create_json_input(self):
        """This will create the json input for the Watson Translator. This should never be called alone.  
        
        Returns:
            [json] -- json structured input comprised of class features. 
        """
        if self.input_lang != "English" and self.output_lang != "English":
            return "One language must be english"

        model = lang_mapping[self.input_lang]
        model += '-'
        model += lang_mapping[self.output_lang]
        input_dict = {"text": self.input_text,
                      "model_id": model}
        return json.dumps(input_dict)

    def get_output_text(self):
        """Method to make a call to the Watson Translator. The constructor must be called first. 
        
        Returns:
            [json] -- json of translated text. 
        """
        API_ENDPOINT = self.url + '/v3/translate?version=2018-05-01'
        API_KEY = self.api_key
        HEADER = {"Content-Type": "application/json"}
        data = self.create_json_input()
        # sending post request and saving response as response object
        r = requests.post(url=API_ENDPOINT, data=data,
                          auth=HTTPBasicAuth("apikey", API_KEY), headers=HEADER)
        pastebin_url = r.text
        return pastebin_url
