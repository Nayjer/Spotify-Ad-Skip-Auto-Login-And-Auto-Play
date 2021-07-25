from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import requests
import webbrowser
import time

track = "https://open.spotify.com/playlist/37i9dQZF1DWWQRwui0ExPn"  # spotify-playlist you want to hear
username = ""  # username or mail address of your spotify account
password = ""  # password of your spotify account
CLIENT_ID = ""  # client id and secret you receive when creating an app
CLIENT_SECRET = ""
redirect_url = "www.google.de" # redirect-link where you receive the auth code, also need to be set in the app from the developer tool 
scopes = "user-read-playback-state"  
driver = webdriver.Chrome()
driver.maximize_window()

webbrowser.open_new_tab(
    "https://accounts.spotify.com/authorize?client_id=" + CLIENT_ID + "&response_type=code&redirect_uri=https://www"
                                                                      ".google.de&scope=" + scopes)
CODE = input("Code:")  # code you receive as a get parameter in the google-link, type it in here

tokens = requests.post("https://accounts.spotify.com/api/token", data={"grant_type": "authorization_code",
                                                                       "code": CODE,
                                                                       "redirect_uri": redirect_url,
                                                                       "client_id": CLIENT_ID,
                                                                       "client_secret": CLIENT_SECRET}
                       )

answer = tokens.json()
token = answer['access_token']  # token we need to connect with endpoints
headers = {"Authorization": "Bearer " + token}


def check_ad():  # checks when its playing an ad
    req = requests.get("https://api.spotify.com/v1/me/player/currently-playing", headers=headers)
    json_req = req.json()
    status = json_req["currently_playing_type"]
    if status == "ad":
        return True
    else:
        return False


def log_in():  # logs into spotify and starts the playlist
    driver.get("https://accounts.spotify.com/en/login?continue=" + track)
    username_field = driver.find_element_by_name("username")
    username_field.clear()
    username_field.send_keys(username)
    password_field = driver.find_element_by_name("password")
    password_field.clear()
    password_field.send_keys(password)
    driver.find_element_by_id("login-button").send_keys(Keys.ENTER)
    play_button_css = 'button[data-testid="play-button"]'
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, play_button_css))
    )
    element = driver.find_element_by_css_selector(play_button_css)
    element.send_keys(Keys.ENTER)
    element.send_keys(Keys.SPACE)


def log_out(): # closes the driver instance and stops the program
    driver.quit()
    exit()


log_in()
time.sleep(5)

while True:
    try:
        if check_ad(): # checks permanently if there's an ad, if so, then this program gets closed and re-open, why not just log_in() again? probably spotify detects a bot or it is to fast
            log_out()
        else:
            continue
    except (ValueError, KeyError, ConnectionError,):
        log_out()
