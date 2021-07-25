# Spotify-Add-Skip-and-Auto-Login

The idea behind this script is, that everytime you re-open the spotify website (or press F5), the ad-counter gets refreshed, but only then if you hear an ad actually. So this script should automate this process. With selenium we manage to log out and into spotify (to reset the ads) and play a playlist or song and with the spotify API we can dedect if theres currently an ad or song played. We cant use the spotify API for playing a song, because for this premium is required and then this script would be useless. But this script has some issues. The first is, that you can only play a playlist or song static again and again and not dynamically. So, if theres an ad and the program re-opens, you start from the beginning of the playlist. But this could be easily fixed, with selenium or with the api, when you edit the playlist. The other issue is, that you need to type the auth code again into cmd after reopeing, but this could also be fixed. Spotipy has a way that the code gets automatically transmitted into the script. Its just an get parameter in a link.

Step for step guide:

1. Install the latest version of google chrome https://www.google.com/intl/de/chrome/
2. Install the suitable version of google chromedriver for your chrome version (e.g. version 88 belongs to version 88) https://chromedriver.chromium.org/
3. Put the chromedriver executable in a known directory and append it as a PATH variable with the command setx PATH "%PATH%;C:\bin", if in C:\bin is the driver
4. Install/Update python3 and append in to the path variable (you can choose it in the installation process) https://www.python.org/downloads/
5. Install selenium with: pip3 install selenium
6. Create an app on https://developer.spotify.com/dashboard/applications There you recive your id and secret
7. Go to Eddit Setting -> Redirect URIs and set it to any URI, what you also need to set up in the script
