import requests
import json

class Entry:
    word=''
    phonetic=''
    origin=''
    meanings=[]

class Meaning:
    def __init__(self,part_of_speech, definition, example, synonyms, antonyms):
        self.part_of_speech=part_of_speech
        self.definition=definition
        self.example=example
        self.synonyms=synonyms
        self.antonyms=antonyms
        

api_url = "https://api.dictionaryapi.dev/api/v2/entries/en/innocent"
response = requests.get(api_url)
print(response.status_code)

attributes=json.loads(json.dumps(response.json()))
print(attributes)

entries=[]
for item in attributes:
    entry=Entry()
    word=item.get('word')
    phonetic=item.get('phonetic','')
    if(not phonetic):
        for phntc in item['phonetics']:
            p=phntc.get('text','')
            if(p):
                phonetic=p
    
    origin=item.get('origin','')
    entry.word=word
    entry.phonetic=phonetic


    meanings=[]
    for meaning in item['meanings']:
        part_of_speech=meaning['partOfSpeech']
        synoyms=meaning['synonyms']
        antonyms=meaning['antonyms']
        for definition in meaning['definitions']:
            meanings.append(Meaning(part_of_speech,definition['definition'],definition.get('example',''),synoyms, antonyms))
    entry.meanings=meanings
    entries.append(entry)
 
for entry in entries:
    print( f'''
    {entry.word}
    {entry.phonetic}
    '''.lstrip())

    for meanings in entry.meanings:
        print( f'''
        {meanings.part_of_speech}
        {meanings.definition}
        {meanings.example}
        {meanings.synonyms}
        {meanings.antonyms}
        '''.lstrip())

def get_formatted_attributes(attributes):
    return '''
'''.lstrip()


