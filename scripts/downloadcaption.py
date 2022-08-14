from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import JSONFormatter

transcript = YouTubeTranscriptApi.get_transcript("qBdieWfouZM")

formatter = JSONFormatter()

text_formatted = formatter.format_transcript(transcript)

with open('20220714.json', 'w', encoding='utf-8') as JSON_file:
    JSON_file.write(text_formatted)
