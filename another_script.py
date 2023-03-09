from deepgram import Deepgram
import asyncio, json
import datetime
from docx import Document
from htmldocx  import HtmlToDocx
import re


DEEPGRAM_API_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxx'
FILE_NAME = 'SERVICE_1_TEST1.mov'


async def main():
    # Initializes the Deepgram SDK
    deepgram = Deepgram(DEEPGRAM_API_KEY)
    # Open the audio file
    with open(FILE_NAME, 'rb') as audio:
        # ...or replace mimetype as appropriate
        source = {'buffer': audio, 'mimetype': 'video/mov'}
        #response = await deepgram.transcription.prerecorded(source, {'punctuate': True,'diarize':True,'paragraphs':True,'tier':'enhanced'})
        #response = await deepgram.transcription.prerecorded(source, {'tier':'base','model':'general','punctuate': True,'diarize':True,'utterances':True,'utt_split':0.3,'max_speakers':2,'numerals':True,'detect_language':True})

        #  RANGE BETWEEN 1.6 AND 1.9
        
        response = await deepgram.transcription.prerecorded(source, {'tier':'base','model':'general','punctuate': True,'diarize':True,'max_speakers':2,'numerals':True,'detect_language':True,'multichannel':True,'paragraphs':True,'utterances':True,'utt_split':0.959})
        document = Document()
        new_parser = HtmlToDocx()
        filename = FILE_NAME.split(".")
        html = "FILE NAME:&nbsp;-----"+filename[0]+"<br><br>"
        #print(response)
        for data in response['results']['utterances']:
            transcript = data['transcript']
            result = "Speaker"+str(data['speaker'])+": "+transcript+"\n"
            print(result)
            
            for word in data['words']:
                #print(word['punctuated_word'])
                if word['punctuated_word'] in transcript and word['confidence'] < 0.90:
                    #transcript = transcript.replace(word['punctuated_word'],'<b><u>'+word['punctuated_word']+'</u></b>\n')
                    transcript = re.sub(r'\b%s\b' % re.escape(word['punctuated_word']), '<b><u>'+word['punctuated_word']+'</u></b>', transcript)
            html += "["+str(datetime.timedelta(seconds=int(data['start'])))+"]<br>"
            html += "<b>Speaker"+str(data['speaker'])+":</b> &nbsp;"+transcript+"<br><br>"
            #print(html)
        html+= '[END OF FILE:&nbsp;-----'+filename[0]+']' 
            
        #new_parser.add_html_to_document(html, document)
        #document.save(filename[0]+'.docx')
        #document.save('demo.docx')
asyncio.run(main())




