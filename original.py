from deepgram import Deepgram
import asyncio, json
import datetime

DEEPGRAM_API_KEY = 'xxxxxxxxxxxxxxxxxxxxx'
PATH_TO_FILE = 'SERVICE_2_TEST1.mov'

async def main():
    # Initializes the Deepgram SDK
    deepgram = Deepgram(DEEPGRAM_API_KEY)
    # Open the audio file
    with open(PATH_TO_FILE, 'rb') as audio:
        # ...or replace mimetype as appropriate
        source = {'buffer': audio, 'mimetype': 'video/mov'}
        #response = await deepgram.transcription.prerecorded(source, {'punctuate': True,'diarize':True,'paragraphs':True})
        response = await deepgram.transcription.prerecorded(source, {'tier':'enhanced','model':'general','punctuate': True,'diarize':True,'max_speakers':3,'numerals':True,'detect_language':True,'multichannel':True,'paragraphs':True})
        
        #print(json.dumps(response, indent=4))
        #transcript = response['results']['channels'][0]['alternatives'][0]['paragraphs']['transcript']
        #with open('SERVICE_1_TEST1.txt','w') as f:
        #    f.write(transcript)

        #print(response['results']['channels'][0]['alternatives'][0]['paragraphs']['paragraphs'])
        result = response['results']['channels'][0]['alternatives'][0]['paragraphs']['paragraphs']
        #print(response['results']['channels'][0]['alternatives'][0]['paragraphs'])
        words = response['results']['channels'][0]['alternatives'][0]['words']

        transcript = ''
        low_confiedence_word = ''
        for data in result:

            transcript += "["+str(datetime.timedelta(seconds=int(data['start'])))+"]\n"
            list_of_values = ''.join(a_dict['text'] for a_dict in data['sentences'])
            transcript += "speaker"+str(data['speaker'])+":"+list_of_values+"\n\n"
        transcript += '\nLow Confidence Word:\n'
        for word in words:
            #print(word['confidence'],word['word'])
            if word['confidence'] < 0.90:
                transcript += word['word']+'  '

        f = open("demofile3.txt", "w")
        f.write(transcript)
        f.close()
        #print(transcript)
        #print(words)
        #'c---6049047288'
        #'acc---045810170829'
        #cif--336652061
        #ac--010020648174
        #12431.38
        #189167.41

asyncio.run(main())

