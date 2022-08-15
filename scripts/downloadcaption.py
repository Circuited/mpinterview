from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import JSONFormatter
import json

user_input = input("Enter the path of your file: ")

with open(user_input) as file:
	data = json.load(file)

##transcript = YouTubeTranscriptApi.get_transcript("qBdieWfouZM")
##
##formatter = JSONFormatter()
##
##text_formatted = formatter.format_transcript(transcript)
##
##with open('20220714.json', 'w', encoding='utf-8') as JSON_file:
##    JSON_file.write(text_formatted)

for indexNumber in range(36,55):
    transcript = YouTubeTranscriptApi.get_transcript(data[str(indexNumber)]['URL'][-11:])
    formatter = JSONFormatter()
    text_formatted = formatter.format_transcript(transcript)
    fileName = data[str(indexNumber)]['Upload data'][:10]+'.json'
    with open(fileName, 'w', encoding='utf-8') as JSON_file:
        JSON_file.write(text_formatted)
