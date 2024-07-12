import langcodes

def find_language_tag(text):
    lang_tag = langcodes.find(text)  # Output: 'en'
    return lang_tag

text = "Bonjour, comment vas-tu?"
print(find_language_tag(text))  # Output: 'fr'

text = "Hello, how are you?"
print(find_language_tag(text))  # Output: 'en'
