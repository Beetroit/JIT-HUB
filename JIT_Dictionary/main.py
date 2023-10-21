import requests
import json

class Entry:
    word=''
    phonetic=''
    origin=''
    meanings=[]

    def __str__(self):
        return f'{self.word}\n{self.phonetic}\n{self.origin}\n{self.meanings}'

class Meaning:
    def __init__(self,part_of_speech, definition, example, synonyms, antonyms):
        self.part_of_speech=part_of_speech
        self.definition=definition
        self.example=example
        self.synonyms=synonyms
        self.antonyms=antonyms

    def __str__(self):
        return f'{self.part_of_speech}\n{self.definition}\n{self.example}\n{self.synonyms}\n{self.antonyms}'

def get_attributes(word):
    api_url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(api_url)
    attributes=json.loads(json.dumps(response.json()))

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
        entry.origin=origin

        meanings=[]
        for meaning in item['meanings']:
            part_of_speech=meaning['partOfSpeech']
            synoyms=meaning['synonyms']
            antonyms=meaning['antonyms']
            for definition in meaning['definitions']:
                meanings.append(Meaning(part_of_speech,definition['definition'],definition.get('example',''),synoyms, antonyms))
        entry.meanings=meanings
        entries.append(entry)
        
    return entries[1]

print(get_attributes('set'))

