from deepgram import Deepgram
import asyncio, json
import datetime
from docx import Document
from htmldocx  import HtmlToDocx
import re


DEEPGRAM_API_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxx'
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
        response = await deepgram.transcription.prerecorded(source, {'tier':'enhanced','model':'general','punctuate': True,'diarize':True,'max_speakers':2,'numerals':True,'detect_language':True,'multichannel':True,'paragraphs':True})
        document = Document()
        new_parser = HtmlToDocx()
        filename = FILE_NAME.split(".")
        html1 = "FILE NAME:&nbsp;-----"+filename[0]+"<br><br>"
        html = ""
        
        result = response['results']['channels'][0]['alternatives'][0]['paragraphs']['paragraphs']

        for data in result:
            html += "[" + str(datetime.timedelta(seconds=int(data['start']))) + "]<br>"
            html += "<b>Speaker" + str(data['speaker']) + ":</b> "
            html += " ".join(a_dict['text'] for a_dict in data['sentences'])+"<br><br>"
        html += "[END OF FILE:&nbsp;-----"+filename[0]+"]"

        new_parser.add_html_to_document(html, document)
        document.save(filename[0]+'-ENHANCEDMODEL-02-12-2022.docx')
        document.save('demo.docx')
asyncio.run(main())




