from user import User
import json

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

new_user = User('Lia')
new_user.add_movie('Field Notes', 'Porn')
new_user.add_movie('Spreequell', 'Porn')
new_user.add_movie('Cherry', 'Rule 34 Porn')

# print(new_user.movies)

print(new_user.name)
for movie in new_user.movies:
    print('Movie: {} from genre: {}'.format(movie.name, movie.genre))