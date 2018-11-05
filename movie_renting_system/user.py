from movie import Movie


class User:
    def __init__(self, name):
        self.name = name
        self.movies = []

    def __repr__(self):
        return "<User: {}>".format(self.name)

    def add_movie(self, name, genre):
        movie = Movie(name, genre, False)
        self.movies.append(movie)

    def delete_movie(self, name):
        self.movies = list(filter(lambda movie: movie.name != name, self.movies))

    def watched_movies(self):
        # calculate a list of movies that have been watched
        # initialize an empty list, iterate over self.movies
        # if movie.watched is true, add it to the list, return list
        return list(filter(lambda movie: movie.watched, self.movies))

    def json(self):
        return {
            'name': self.name,
            'movies': [
                movie.json() for movie in self.movies
            ]
        }

    # def save_to_file(self):
    #     with open("{}.txt".format(self.name), "w") as file:
    #         file.write(self.name + "\n")
    #         for movie in self.movies:
    #             # file.write(movie.name + "," + movie.genre + "," + str(movie.watched))
    #             file.write("{},{},{}\n".format(movie.name, movie.genre, str(movie.watched)))
    #
    # @classmethod
    # def load_from_file(cls, filename):
    #     with open(filename, 'r') as f:
    #         content = f.readlines()  # get all lines from loaded file
    #         username = content[0]  # get username from the first line of the file
    #         movies = []  # empty list for movies from loaded file
    #         for line in content[1:]:  # starts from the first element = first line with movies
    #             movie_data = line.split(",")
    #             movies.append(Movie(movie_data[0], movie_data[1], movie_data[2] == "True"))
    #
    #         user = User(username)
    #         user.movies = movies
    #         return user
