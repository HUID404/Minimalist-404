import requests

video_url = 'https://example.com/video.mp4'

response = requests.get(video_url)
if response.status_code == 200:
    print(response.url)
else:
    print('Failed to fetch video URL.')
