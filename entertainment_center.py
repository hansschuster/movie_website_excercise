import media
import fresh_tomatoes


# Creating instances of class Movie with arguments
# title, storyline, poster_image_url and trailer_youtube_url
carnage = media.Movie(
    "Carnage",
    "Two sets of parents discussing a fight of their kids,"
    " slowly escalating from civility to rudeness",
    "https://upload.wikimedia.org/wikipedia/en/3/3a/Carnage_film_poster.jpg",
    "https://www.youtube.com/watch?v=ZPX6-4Bo7XU")

gladiator = media.Movie(
    "Gladiator",
    "The story of betrayed Roman General Maximus Meridius,"
    " fighting back as a slave and gladiator",
    "https://upload.wikimedia.org/wikipedia/en/8/8d/Gladiator_ver1.jpg",
    "https://www.youtube.com/watch?v=owK1qxDselE")

braveheart = media.Movie(
    "Braveheart",
    "William Wallace, a 13th-century Scottish rebel,"
    " leading Scotland to independance and avenging his murdered wife",
    "https://upload.wikimedia.org/wikipedia/en/5/55/Braveheart_imp.jpg",
    "https://www.youtube.com/watch?v=wj0I8xVTV18")

dark_knight = media.Movie(
    "Batman - The Dark Knight",
    "The fight of Batman against the Joker",
    "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
    "https://www.youtube.com/watch?v=_PZpmTj1Q8Q")

life_is_beautiful = media.Movie(
    "Life Is Beautiful",
    "Set in Fascist Italy, this film tells the story of a Jewish Italian"
    " family in a concentration camp, and how the father shields their son by"
    " pretending that everyone simply conspired to play an elaborate game.",
    "https://upload.wikimedia.org/wikipedia/en/7/7c/Vitaebella.jpg",
    "https://www.youtube.com/watch?v=pAYEQP8gx3w")

rocky = media.Movie(
    "Rocky",
    "Rocky Balbo, a local boxer from Philadelphia,"
    " gets a chance to box against the heavyweight world champion",
    "https://upload.wikimedia.org/wikipedia/en/1/18/Rocky_poster.jpg",
    "https://www.youtube.com/watch?v=7RYpJAUMo2M")


# Storing instances in list. Calling function to create html file
# and open it in webbrowser
movies = [
    carnage, braveheart, life_is_beautiful,
    gladiator, dark_knight, rocky]
fresh_tomatoes.open_movies_page(movies)
