import spacy
nlp = spacy.load('en_core_web_md')

# Creating Movie object class
class Movie:
    
    similarity = 0

    # Initializer with variables title and description
    def __init__(self, title, description):
        self.title = title
        self.description = description
    
    # Function to find and store similarity index of object description with the user's movie description
    def compare_movies(self):
        self.similarity = nlp(self.description).similarity(nlp(user_movie.description))

# Function to compare similarity of each movie in the list's description with the user's last watched movie description
# Creates a list of each movie in the list and its similarity index
# Prints the title of the movie with the highest similarity
def recommendation():
    similarity_list = []
    for movie in movie_list:
        movie.compare_movies()
        similarity_list.append((movie.similarity, movie.title))
    similarity_list.sort()
    print(f"Watch next: {similarity_list[-1][1]}")


# Setting up variables for the user's last movie watched, and the list of movies available next
movie_list = []
user_movie = Movie("Planet Hulk", "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hull lands on the planet Sakaar where he is sold into slavery and trained as a gladiator.")

# Read movies.txt and turns each line into a movie object, storing its title and description
# Adds each movie to a list of objects
with open('movies.txt', 'r') as f:
    for line in f:
        movie = line.split(" :")
        movie = Movie(movie[0], movie[1])
        movie_list.append(movie)

# Runs program to print the most similar movie as a 'watch next' recommendation
recommendation()
