from utils import commands, lyrics
import spotipy
from utils.config import sp
from colorama import Fore, Style


def main():
    global user_profile
    print(Fore.GREEN + """ 
 ## ##   ####       ####   ### ###  ##  ##   
##   ##   ##         ##     ##  ##  ##  ##   
##        ##         ##     ##      ##  ##   
##        ##         ##     ## ##    ## ##   
##        ##         ##     ##        ##     
##   ##   ##  ##     ##     ##        ##     
 ## ##   ### ###    ####   ####       ##     
                                             
 """ + Style.RESET_ALL)
    try:
        user_profile = sp.current_user()
        print("Successfully authenticated. User profile:")
        print(f"Display name: {user_profile['display_name']}")
        print(f"User ID: {user_profile['id']}")

    except spotipy.SpotifyException as e:
        print(f"Error accessing Spotify API: {e}")
    while True:

        try:
            user_input = input("Clify > ")
            if user_input.split()[0] == "nowplaying":
                commands.nowplaying(user_input.split())
            elif user_input.split()[0] == "search":
                commands.spotify_search(user_input.split())
            elif user_input == "pause":
                commands.pause()
            elif user_input == "play":
                commands.play()
            elif user_input == "skip":
                commands.skip()
            elif user_input == "prev":
                commands.prev()
            elif user_input == "shuffle":
                commands.shuffle()
            elif user_input == "timer":
                commands.timer()
            elif user_input == "recs":
                commands.recs()
            elif user_input == "lyrics":
                lyrics.get_lyrics()
            elif user_input == "createplist":
                commands.create_playlist(user_profile)
            elif user_input == "playlists":
                commands.playlists()
            elif user_input == "library":
                commands.show_library()
            elif user_input.split()[0] == "loop":
                commands.loop(user_input.split()[1])
            elif user_input == "close":
                break
            elif user_input == "help":
                print("""=== HELP ===
    
>>> General <<<
                  
search: Search spotify for a specific song. Use '-a' to show the album for each search result.
nowplaying: Shows the song that is playing. Use '-a' to show the album. Use '-l' to add song to library.
lyrics: Shows the lyrics of currently playing song. 
library: Displays the last 20 tracks you added to your library.
createplist: Create a new playlist.
playlists: Allows you to view all the songs in a playlist from your library.
recs: Shows list of recommended songs. 
timer: Pause the song after the specified duration.
close: Closes the program.
                  
>>> Playback Controls <<<
                      
play: Resume playback or play recently played tracks if no current playback.
pause: Pause the currently playing song.
skip: Skips to the next song.
prev: Skips to the previous song.
shuffle: Toggles the shuffle state.


For more info, read the README.md file.""")
            else:
                print("Not a command! Type 'help' for a list of commands.")
        except (ValueError, IndexError) as e:
            print(f"An error has occured: {e}. If you pressed enter without inputting a command, that's why.")

if __name__ == "__main__":
    main()
