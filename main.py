#imports
from display import print_menu,print_header,clear #importing functions from another file
from album import Album #importing a class (that is including methods) from another file
from song import Song
import pickle

#globals
# DECLARE A CATALOG VARIABLE (LIST)
catalog = []  #not a simple variable dont need to use global
#simple variable need to use global
album_count = 0
albumid = 0

#functions
def deserialize_data():
    global album_count

    try:
        reader = open('songMngr.data', 'rb')  # rb = read binary
        temp_list = pickle.load(reader) #load into memory
        reader.close()

        for prod in temp_list:
            catalog.append(prod)
            album_count += 1

        # get the last used id, and increase by 1
        last = catalog[-1]
        album_count2 = last.id + 1

        how_many = len(catalog)
        print("** Read: " + str(how_many) + " albums")

    except:
        print("no data file found")


def find_album(album_id):
    #find the album with that id
    found = False
    for item in catalog:
        if(album_id == item.id):
            the_album = item #saving the found album
            found = True
            return the_album

    if(not found):
        print("Not a valid id. Try again.")
        return found


def register_album_set(title):
    temp = input("Please provide %s"%title)
    return temp


def serialize_data():
    try:
        writer = open('songMngr.data', 'wb')  # wb = write binary
        pickle.dump(catalog, writer) #get infomation from memory and dump it into this file
        writer.close()
        print("** Data serialized!")
    except:
        print("** Error, data not saved")


def validate_input(myType,header_title):
    notValidate = True

    while notValidate:
        try:
            if (myType == "float"):
                temp = float(input(header_title))
            elif(myType == "int"):
                temp = int(input(header_title))
            notValidate = False
        except ValueError:
            print("** Error: Invalid Number. Try again")
        except:
            print("\nPlease enter a[n] {}".format(myType))
        else:
            return temp



#option 1
def register_album():
    print_header("Register a new Album")
    # title, genre, artist, release_year, price, album_art, record_label
    title = register_album_set("Title: ")
    genre = register_album_set("Genre: ")
    artist = register_album_set("Artist Name: ")
    release_year = validate_input("int", "Please enter the Release Year: ")
    price = validate_input("float", "Please enter price: $")
    album_art = register_album_set("Album Art URL: ")
    related_artist = register_album_set("Related Artist: ")
    record_label = register_album_set("Record Label: ")
    global album_count #import this global variable into the function
    album_count += 1
    album = Album(album_count, title, genre, artist, release_year, price, album_art, related_artist, record_label)
    # print(album)

    # PUSH THE ALBUM INTO THE LIST
    catalog.append(album)

    print("** album created!".title())
    # the_album = Album()
    # the_album.title = title
    # the_album.genre = genre
    # the_album.artist = artist


#OPTION 2
def register_song():

    #let the user choose an album
    print_albums()
    print("\n")
    album_id = validate_input("int", "Please provide the album id: ")

    #find the album with that id
    # found = False
    # for item in catalog:
    #     if(album_id == item.id):
    #         found = True
    #         the_album = item #saving the found album

    # if(not found):
    #     print("Not a valid id. Try again.")
    #     return

    the_album = find_album(album_id)
    if(the_album == False):
        return

    #create the song
    print_header("Register a new Song for {}".format(the_album.title.title()))
    # id, title, featured_artist, length, written_by
    title = register_album_set("Title: ")
    featured_artist = register_album_set("a Featured Artist: ")
    length_of_track = validate_input("int", "Please enter the length of track in seconds: ")
    written_by = register_album_set("the song author: ".title())

    song = Song(album_id, title, featured_artist, length_of_track, written_by)
    #push the song to the album list
    the_album.add_song(song)
    print("\n {} was registered!".title().format(song.title))


#FINISH OPTION 3
def print_albums():
    print_header("Your current albums".title())

    for album in catalog:
         print(f"Album ID: {album.id} | Title: {album.title.title()} | Year: {album.release_year} | Genre: {album.genre} | Artist: {album.genre} | Price: ${album.price:.2f}")
        # print(f"Album ID: {album.id} | Title: {album.title.title()} | Year: {album.release_year} | Genre: {album.genre} | Artist: {album.genre} | Price: {album.price} | Album Art: {album.album_art} | Related Artist: {album.related_artist} | Record Label: {album.record_label}")
    

  #option 4 - print songs in albums
def print_songs():
    print_albums()
    album_id = validate_input("int", "To View songs, please provide the album id: ")
    global albumid
    albumid=album_id
    the_album = find_album(album_id)

    if(the_album == False):
        return
    elif(len(the_album.songs) <= 0):
        print("\n No Tracks in this album.")
    else:
        counter=0
        for item in the_album.songs:
            counter += 1
            print("Track: {}, Title: {}, Featured Artist: {}, length: {}s, Written By: {}".format(counter, item.title.title(), item.featured_artist.title(), item.length_of_track, item.written_by.title()))


#option 5: count all the songs
def count_all_songs():
    print_header("Your total number of songs")
    total_count_of_songs=0
    for album in catalog:
        temp = len(album.songs)
        total_count_of_songs += temp
    print("Total songs in audioMgr: {}".format(total_count_of_songs))


#option 6
def print_all():
    print_header("print albums and songs".title())
    for album in catalog:
        print("\nAlbum-{}: {}".format(album.id, album.title.title()))

        # if there are no songs in the album else print songs
        if (len(album.songs) == 0):
            print("No tracks in album: {}".format(album.title.title()))
        else:
            counter = 0
            for item in album.songs:
                counter += 1
                print("Track: {}, Title: {}, Featured Artist: {}, length: {}s, Written By: {}".format(counter, item.title.title(), item.featured_artist.title(), item.length_of_track, item.written_by.title()))


# print("[7] Total $ in the catalog")
def total_cost():
    print_header("Your total cost")
    counter = 0
    for album in catalog:
        temp = album.price
        counter += temp
    print("Your total album cost is: ${:.2f}".format(counter))


# print("[8] Most expensive album")
def most_expensive_album():
    print_header("Your most expensive album")
    # all_price = []

    album_id = catalog[0].id
    most_expensive = catalog[0].price
    album_title = catalog[0].title
    for album in catalog:
        if(most_expensive < album.price):
            most_expensive = album.prices
            album_title = album.title
            album_id = album.id
    # all_price.append(album.price)
    # most_expensive = max (all_price)
    print("Your most expensive album-{}: {} at ${:.2f}".format(album_id, album_title.title(), most_expensive))


# print("[10] Change the title of an specific album")
def change_album_title():
    """Change the title of an album
    Will ask the user to pick the index of the album
    Then Ask for a new input for the title
    """
    print_header("Change album title")
    print_albums()
    album_id = validate_input("int", "Please pick the album id: ")
    the_album = find_album(album_id)
    if(the_album == False):
        return
    new_album_title = input("\nEnter new title for album: ")
    the_album.title=new_album_title


#print("[11] Change the title of a specific song")
def change_song_title():
    """Change the title of a song inside an album
    Will ask the user to pick the index of the album
    Then ask for a new input for the title
    """
    print_header("Change song title")
    print_songs()
    global albumid
    track_id = validate_input("int", "Please pick the song track: ")
    the_album = find_album(albumid)
    new_song_title = input("\nEnter new song title: ")
    the_album.songs[track_id - 1].title=new_song_title


deserialize_data()
input("Press Enter to continue...")
#instructions
opc = ''
while(opc != 'q'):
    clear()
    print_menu()
    opc = input("Please select an option: ")

    if(opc == '1'):
        register_album()
        serialize_data()
    elif(opc == '2'):
        register_song()
        serialize_data()
    elif(opc == '3'):
        print_albums()
    elif(opc == '4'):
        print_songs()
    elif(opc == '5'):
        count_all_songs()
    elif(opc == '6'):
        print_all()
    elif(opc == '7'):
        total_cost()
    elif(opc == '8'):
        most_expensive_album()
    elif(opc == '10'):
        change_album_title()
        serialize_data()  #save data
    elif(opc == '11'):
        change_song_title()
        serialize_data()
    elif(opc.lower() == 'q'):
        break
    else:
        print("Invalid option. Try again.")
    input("\nPress Enter to continue...")
clear()
print("good byte".title())