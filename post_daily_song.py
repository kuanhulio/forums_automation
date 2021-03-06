from xenposter import create_driver_for_remote, login_to_forums, post_message
from spotipy_random import get_random
import spotipy, datetime, time, json, random

with open("/root/login.json") as login_file:
    login_data = json.load(login_file)

def main():
    if datetime.datetime.now().hour < 12:
        print("It's before 12:00, so I'm not posting anything.")
    elif datetime.datetime.now().hour > 12:
        print("It's after 12:00, so I'm not posting.")
    else:
        driver = create_driver_for_remote(
            "chrome",
            None,
            "192.168.1.100",
            "4444"
        )

        spotify_client = spotipy.Spotify(   
            auth_manager=spotipy.SpotifyClientCredentials(
            client_id=login_data["client_id"],
            client_secret=login_data["client_secret"]
            )
        )

        random_rap_song = get_random(spotify=spotify_client, type="track", genre="rap")["external_urls"]["spotify"]
        random_hiphop_song = get_random(spotify=spotify_client, type="track", genre="hip-hop")["external_urls"]["spotify"]
        random_pop_song = get_random(spotify=spotify_client, type="track", genre="pop")["external_urls"]["spotify"]
        random_rock_song = get_random(spotify=spotify_client, type="track", genre="rock")["external_urls"]["spotify"]

        random_song = random.choice(
            [
                random_rap_song, 
                random_hiphop_song, 
                random_pop_song, 
                random_rock_song
            ]
        )

        login_to_forums(driver, "https://www.edgegamers.com", login_data["username"], login_data["password"], 1, login_data["totp"])
        post_message(driver, "https://www.edgegamers.com/threads/374510/", random_song, 1)
    
while(True):
    main()
    time.sleep(3600) # 1 hour
    print("Sleeping for 1 hour")