from app import media
from app import movie_website

WIKI_PATH = "http://upload.wikimedia.org/wikipedia"
YOUTUBE_URL = "https://www.youtube.com/watch?v="

movies_dict = dict(
    avatar=dict(
        title="Avatar",
        storyline="A paraplegic marine dispatched to the moon Pandora on a \
                  unique mission becomes torn between following his orders \
                  and protecting the world he feels is his home.",
        poster_image=WIKI_PATH + "/id/b/b0/Avatar-Teaser-Poster.jpg",
        trailer_url=YOUTUBE_URL + "5PSNL1qE6VY"
    ),
    ratatouille=dict(
        title="Ratatouille",
        storyline="A rat who can cook makes an unusual alliance with a young \
                  kitchen worker at a famous restaurant.",
        poster_image=WIKI_PATH + "/en/5/50/RatatouillePoster.jpg",
        trailer_url=YOUTUBE_URL + "c3sBBRxDAqk"
    ),
    hunger_games=dict(
        title="Hunger Games",
        storyline="Katniss Everdeen voluntarily takes her younger sister's \
                  place in the Hunger Games, a televised competition in \
                  which two teenagers from each of the twelve Districts of \
                  Panem are chosen at random to fight to the death.",
        poster_image=WIKI_PATH + "/en/4/42/HungerGamesPoster.jpg",
        trailer_url=YOUTUBE_URL + "PbA63a7H0bo"
    ),
    seven_pounds=dict(
        title="Seven Pounds",
        storyline="A man with a fateful secret embarks on an extraordinary \
                  journey of redemption by forever changing the lives of \
                  seven strangers.",
        poster_image=WIKI_PATH + "/en/2/2d/Seven_Pounds_poster.jpg",
        trailer_url="https://www.youtube.com/watch?v=MwrtEI-fcmM"
    ),
    shutter_island=dict(
        title="Shutter Island",
        storyline="It's 1954, and up-and-coming U.S. marshal Teddy Daniels \
                  is assigned to investigate the disappearance of a patient \
                  from Boston's Shutter Island Ashecliffe Hospital. He's \
                  been pushing for an assignment on the island for personal \
                  reasons, but before long he wonders whether he hasn't \
                  been brought there as part of a twisted plot by hospital \
                  doctors whose radical treatments range from unethical to \
                  illegal to downright sinister. Teddy's shrewd \
                  investigating skills soon provide a promising \
                  lead, but the hospital refuses him access to records he \
                  suspects would break the case wide open. As a hurricane \
                  cuts off communication with the mainland, more dangerous \
                  criminals 'escape' in the confusion, and the puzzling, \
                  improbable clues multiply, Teddy begins to doubt \
                  everything - his memory, his partner, even his own sanity.",
        poster_image=WIKI_PATH + "/en/7/76/Shutterislandposter.jpg",
        trailer_url=YOUTUBE_URL + "5iaYLCiq5RM"
    ),
    the_notebook=dict(
        title="The Notebook",
        storyline="The movie focuses on an old man reading a story to an old \
                  woman in a nursing home. The story he reads follows two \
                  young  lovers named Allie Hamilton and Noah Calhoun, who \
                  meet one evening at a carnival. But they are separated by \
                  Allie's parents who disapprove of Noah's unwealthy family, \
                  and move Allie away. After waiting for Noah to write her \
                  for several years, Allie meets and gets engaged to a \
                  handsome young soldier named Lon. Allie, then, with her \
                  love for Noah still alive, stops by Noah's 200-year-old \
                  home that he restored for her, to see if he's okay. \
                  It is evident that they still have feelings for each \
                  other, and Allie has to choose between her fianc&eacute; \
                  and her first love.",
        poster_image=WIKI_PATH + "/en/8/86/Posternotebook.jpg",
        trailer_url=YOUTUBE_URL + "4M7LIcH8C9U"
    ),
    the_pursuit_of_happyness=dict(
        title="The Pursuit of Happyness",
        storyline="Chris Gardner has big dreams for him and his family but \
                  it doesn't seem to come together for him. Chris has an \
                  opportunity to be a stock broker but first he has to go \
                  through a grueling internship which means no pay. Chris \
                  decides to do it but when his wife leaves and he is \
                  evicted, he has to take care of his son on his own. \
                  So they find themselves sometimes living on the street \
                  and struggling to get by. But Chris is determined to make \
                  it.",
        poster_image=WIKI_PATH + "/en/8/81/Poster-pursuithappyness.jpg",
        trailer_url=YOUTUBE_URL + "89Kq8SDyvfg"
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

movie_website.open_movies_page(movies)
