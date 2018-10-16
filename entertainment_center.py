import fresh_tomatoes
import media

iron_man = media.Movie("Iron Man",
                       "2008's Iron Man tells the story of Tony Stark, a billionaire industrialist and genius inventor who is kidnapped and forced to build a devastating weapon.",
                       "https://upload.wikimedia.org/wikipedia/en/7/70/Ironmanposter.JPG",
                       "https://www.youtube.com/watch?v=8hYlB38asDY")

iron_man_2 = media.Movie("Iron Man 2",
                          "Iron Man 2 is a 2010 superhero film, based on the Marvel Comics superhero of the same name. It is a sequel to Iron Man.",
                          "https://upload.wikimedia.org/wikipedia/en/e/ed/Iron_Man_2_poster.jpg",
                          "https://www.youtube.com/watch?v=wKtcmiifycU")

iron_man_3 = media.Movie("Iron Man 3",
              "Tony Stark encounters a formidable foe called the Mandarin. After failing to defeat his enemy, he embarks on a journey with relentless consequences and a suit that ceases to exist.",
              "https://upload.wikimedia.org/wikipedia/en/d/d5/Iron_Man_3_theatrical_poster.jpg",
              "https://www.youtube.com/watch?v=f_h95mEd4TI")

black_panther = media.Movie("Black Panther",
                            "T'Challa, heir to the hidden but advanced kingdom of Wakanda, must step forward to lead his people into a new future and must confront a challenger from his country's past.",
                            "https://upload.wikimedia.org/wikipedia/en/0/0c/Black_Panther_film_poster.jpg",
                            "https://www.youtube.com/watch?v=dxWvtMOGAhw")

avengers_infinity_war = media.Movie("Avengers: Infinity War",
                                    "The Avengers and their allies must be willing to sacrifice all in an attempt to defeat the powerful Thanos before his blitz of devastation and ruin puts an end to the universe.",
                                    "https://upload.wikimedia.org/wikipedia/en/4/4d/Avengers_Infinity_War_poster.jpg",
                                    "https://www.youtube.com/watch?v=6ZfuNTqbHE8")

venom = media.Movie("Venom",
                    "When Eddie Brock acquires the powers of a symbiote, he will have to release his alter-ego Venom to save his life.",
                    "https://upload.wikimedia.org/wikipedia/en/0/05/Venom_poster.jpg",
                    "https://www.youtube.com/watch?v=u9Mv98Gr5pY")

ramona_and_beezus = media.Movie("Ramona and Beezus",
                     "An adventurous young girl uses her imagination to escape her reality, that is quickly spinning out of reach.",
                     "https://upload.wikimedia.org/wikipedia/en/9/90/Ramona_and_Beezus_Poster.jpg",
                     "https://www.youtube.com/watch?v=VP5FW5KA6Go")

paper_towns = media.Movie("Paper Towns",
               "After an all-night adventure, Quentin's lifelong crush, Margo, disappears, leaving behind clues that Quentin and his friends follow on the journey of a lifetime.",
               "https://upload.wikimedia.org/wikipedia/en/0/00/Paper_Towns_%28film%29.jpg",
               "https://www.youtube.com/watch?v=rFGiHm5WMLk")

fifty_shades_of_grey = media.Movie("Fifty Shades of Grey",
                     "Literature student Anastasia Steele's life changes forever when she meets handsome, yet tormented, billionaire Christian Grey.",
                     "https://upload.wikimedia.org/wikipedia/en/7/73/Fifty_Shades_of_Grey_poster.jpg",
                     "https://www.youtube.com/watch?v=SfZWFDs0LxA")

#print(iron_man.storyline
#iron_man.show_trailer()

movies = [iron_man, iron_man_2, iron_man_3, black_panther, avengers_infinity_war, venom, ramona_and_beezus, paper_towns, fifty_shades_of_grey]
fresh_tomatoes.open_movies_page(movies)
