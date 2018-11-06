from user import User
import json
import os

def menu():
    # ask for the users name
    user_name_input = input('Hello! Enter your name: ')
    print(user_name_input)

    # if it already exists, welcome them and load their data
    filename = '{}.txt'.format(user_name_input)
    if file_exists(filename):
        with open(filename, 'r') as file:
            json_data = json.load(file)
        user = User.user_from_json(json_data)
    # if not, create user object
    else:
        user = User(user_name_input)

    user_input = input("Enter 'a' to add a movie, "
                       "'s' to see a list of movies,"
                       "'w' to set a movie as watched, "
                       "'d' to delete a movie,"
                       "'l' to see the list of watched movies,"
                       " or 'q' to save and quit: ")

    while user_input != 'q':
        if user_input == 'a':
            movie_name = input('Enter a movie name: ')
            movie_genre = input('Enter the movie genre: ')
            user.add_movie(movie_name, movie_genre)
        elif user_input == 's':
            for movie in user.movies:
                print("Name: {}, Genre: {}, Watched: {}".format(movie.name, movie.genre, movie.watched))
        elif user_input == 'w':
            movie_name = input('Enter the movie you have watched: ')
            user.set_watched(movie_name)
        elif user_input == 'd':
            movie_name = input('Enter the movie name to delete: ')
            user.delete_movie(movie_name)
        elif user_input == 'l':
            for movie in user.watched_movies():
                print("Name: {}, Genre: {}, Watched: {}".format(movie.name, movie.genre, movie.watched))

        user_input = input("Enter 'a' to add a movie, "
                           "'s' to see a list of movies,"
                           "'w' to set a movie as watched, "
                           "'d' to delete a movie,"
                           "'l' to see the list of watched movies,"
                           " or 'q' to save and quit: ")

        with open(filename, 'w') as file:
            json.dump(user.json(), file)

    # give them a list of options:
        # add a movie
        # see list of movies
            # set a movie as watched
            # delete a movie by name
        # see list of watched movies
        # save and quit
    pass


def file_exists(filename):
    return os.path.isfile(filename)


menu()







# with open('my_file.txt', 'r') as file:
#     json_data = json.load(file)
#     user = User.user_from_json(json_data)
#     print(user.json())

# user = User('Mia')
# user.add_movie('Rotkaeppchen', 'Fantasy')
# user.add_movie('Die Schoene und das Biest', 'Fantasy')

# print(user.json())

# with open('my_file.txt', 'w') as f:
#     json.dump(user.json(), f)

# print(user.watched_movies())

# user = User.load_from_file("Jule.txt")
# print(user.name)
# print(user.movies)

# new_user = User('Lia')
# new_user.add_movie('Field Notes', 'Fantasy')
# new_user.add_movie('Spreequell', 'Sci-Fi')
# new_user.add_movie('Cherry', 'Documentary')
#
# # print(new_user.movies)
#
# print(new_user.name)
# for movie in new_user.movies:
#     print('Movie: {} from genre: {}'.format(movie.name, movie.genre))
