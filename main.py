from deepgram import Deepgram
import asyncio, json
import datetime

DEEPGRAM_API_KEY = 'xxxxxxxxxxxxxxxxxxx'
PATH_TO_FILE = 'SERVICE_1_TEST1.mov'

async def main():
    # Initializes the Deepgram SDK
    deepgram = Deepgram(DEEPGRAM_API_KEY)
    # Open the audio file
    with open(PATH_TO_FILE, 'rb') as audio:
        # ...or replace mimetype as appropriate
        source = {'buffer': audio, 'mimetype': 'video/mov'}
        response = await deepgram.transcription.prerecorded(source, {'punctuate': True,'diarize':True,'paragraphs':True})
        lst = []
        result = response['results']['channels'][0]['alternatives'][0]['paragraphs']['paragraphs']
        for data in result:
           list_of_values = ''.join(a_dict['text'] for a_dict in data['sentences'])
           lst.append({'speaker':data['speaker'],'start':data['start'],'transcript':list_of_values})
        for element in lst:
            #print(element)
        #print(response['results']['channels'][0]['alternatives'][0]['paragraphs'])
        #print(response)


asyncio.run(main())

