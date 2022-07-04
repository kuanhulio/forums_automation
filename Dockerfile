FROM python:buster

ADD post_daily_song.py /root/post_daily_song.py
ADD xenposter.py /root/xenposter.py
ADD login.json /root/login.json

RUN pip install selenium mintotp spotipy spotipy_random

CMD [ "python", "/root/post_daily_song.py" ]