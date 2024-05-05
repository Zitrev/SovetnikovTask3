from googletrans import Translator
translator = Translator()

def TransLate(text, lang):
    translation = translator.translate(text, dest=lang)
    return translation.text



def LangDetect(txt):
    result = translator.detect(txt)
    return result.lang, result.confidence

def CodeLang(lang):
    lang_codes = {
        'english': 'en',
        'українська': 'uk',
        'japanese': 'ja',
        
    }
    
    lang_lower = lang.lower()
    if lang_lower in lang_codes:
        return lang_codes[lang_lower]
    else:
        for key, value in lang_codes.items():
            if value == lang_lower:
                return key
        return None  

user_text = input("Enter the text you want to translate: ")
target_lang = input("Enter the language you want to translate into: ")

translated_text = TransLate(user_text, CodeLang(target_lang))
print("Translated text:", translated_text)

detected_lang, confidence = LangDetect(user_text)
print("Detected language:", detected_lang)
print("Confidence:", confidence)


code_lang = CodeLang(target_lang)
if code_lang:
    print("Language code:", code_lang)
else:
    print("Language not found in the dictionary.")