# -*- coding: utf-8 -*-
"""
Created on Tue May 5 15:06:45 2020

@author: Deirdre Brennan

This program uses the Wordnik API (https://github.com/wordnik/wordnik-python3) 
to get random words based around the phrase 'Colorless green ideas sleep
furiously," written by Noam Chomsky that a sentence can be syntactically
correct but completely meaningless
(https://en.wikipedia.org/wiki/Colorless_green_ideas_sleep_furiously).
"""

# <<<PLEASE NOTE>>>: The Wordnik API has a rate limit of 5000 requests per hour;
# in order to avoid an HTTP error from making too many requests, please allow 
# some downtime between termination of the program and restarting the program.


from wordnik import *
from pattern.en import singularize, pluralize, conjugate #used to ensure verb and noun are plural
import time
apiUrl = 'http://api.wordnik.com/v4'
apiKey = 'lqg5mrnnvdhe2c4kky53gnnzzc97iwoc4l5utmspy87aedlli'
client = swagger.ApiClient(apiKey, apiUrl)
wordsApi = WordsApi.WordsApi(client)

def generate():
    adj1 = wordsApi.getRandomWord(includePartOfSpeech='adjective').word
    print('got adj1')
    time.sleep(3) #sleep system between each word to prevent too many http requests at once
    adj2 = wordsApi.getRandomWord(includePartOfSpeech='adjective').word
    print('got adj2')
    time.sleep(3)
    
    '''
    The noun and verb are to be plural. In order to ensure that an extra "s" is
    not added to the end of the noun during pluralization, it is singularized first.
    '''
    noun = pluralize(singularize(wordsApi.getRandomWord(includePartOfSpeech='noun').word))
    print('got noun')
    time.sleep(3)
    verb = conjugate(wordsApi.getRandomWord(includePartOfSpeech='verb', hasDictionaryDef='true').word, 'pl')
    print('got verb')
    time.sleep(3)
    adverb = wordsApi.getRandomWord(includePartOfSpeech='adverb').word
    print('got adverb')
    
    sentence = adj1.capitalize() + " " + adj2 + " " + noun + " " + verb + " " + adverb + "."
    #print(sentence)
    return sentence

if __name__ == "__main__":
    print('Generating sentence, please wait.')
    sentence = generate()
    print(sentence)
