import media
import fresh_tomatoes


movies_dict = dict(
    avatar=dict(
        title="Avatar",
        storyline="A marine on an alien planet",
        poster_image="http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
        trailer_url="https://www.youtube.com/watch?v=5PSNL1qE6VY"
    ),
    ratatouille=dict(
        title="Ratatouille",
        storyline="",
        poster_image="http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
        trailer_url="http://www.youtube.com/watch?v=c3sBBRxDAqk"
    ),
    hunger_games=dict(
        title="Hunger Games",
        storyline="",
        poster_image="http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
        trailer_url="http://www.youtube.com/watch?v=PbA63a7H0bo"
    ),
    seven_pounds=dict(
        title="Seven Pounds",
        storyline="",
        poster_image="https://upload.wikimedia.org/wikipedia/en/2/2d/Seven_Pounds_poster.jpg",
        trailer_url="https://www.youtube.com/watch?v=MwrtEI-fcmM"
    ),
    shutter_island=dict(
        title="Shutter Island",
        storyline="",
        poster_image="https://upload.wikimedia.org/wikipedia/en/7/76/Shutterislandposter.jpg",
        trailer_url="https://www.youtube.com/watch?v=5iaYLCiq5RM"
    ),
    the_notebook=dict(
        title="The Notebook",
        storyline="",
        poster_image="https://upload.wikimedia.org/wikipedia/en/8/86/Posternotebook.jpg",
        trailer_url="https://www.youtube.com/watch?v=4M7LIcH8C9U"
    ),
    the_pursuit_of_happyness=dict(
        title="The Pursuit of Happyness",
        storyline="Is based on a true story about a man named Christopher Gardner.",
        poster_image="https://upload.wikimedia.org/wikipedia/en/8/81/Poster-pursuithappyness.jpg",
        trailer_url="https://www.youtube.com/watch?v=89Kq8SDyvfg"
    )

)

movies = []
for movie in movies_dict:
    movies.append(
        media.Movie(
            movies_dict[movie]['title'],
            movies_dict[movie]['storyline'],
            movies_dict[movie]['poster_image'],
            movies_dict[movie]['trailer_url']
        )
    )


fresh_tomatoes.open_movies_page(movies)


