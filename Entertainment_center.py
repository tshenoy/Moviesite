import fresh_tomatoes
import media

dangal = media.Movie("Dangal", "Story of two females wrestlers coached by their wrestler father",
"http://www.reviewrating.org/wp-content/uploads/2016/11/Dangal-Movie-Posters-Aamir-Khan-Stills-in-Dangal-2.jpg",
"https://www.youtube.com/watch?v=x_7YlGv9u1g")
#print (dangal.storyline)
#dangal.show_trailer()
the_departed = media.Movie("The Departed", "young undercover cop and criminal standing on the opposite sides of the law"
                           , "http://www.impawards.com/2006/posters/departed.jpg"
                           , "https://www.youtube.com/watch?v=auYbpnEwBBg")

three_idiots = media.Movie("3 Idiots", "Three friends and their antics at college"
                      ,"https://upload.wikimedia.org/wikipedia/en/d/df/3_idiots_poster.jpg"
                      , "https://www.youtube.com/watch?v=xvszmNXdM4w")

predestination = media.Movie("Predestination","A time travel to prevent terrorist attack"
                  ,"http://www.impawards.com/intl/australia/2014/posters/predestination_ver2.jpg"
                  ,"https://www.youtube.com/watch?v=-FcK_UiVV40")

finding_nemo = media.Movie("Finding Nemo", "Clownfish Marin searching for his son Nemo"
                , "http://fontmeme.com/images/Finding-Nemo-Poster.jpg"
                , "https://www.youtube.com/watch?v=wZdpNglLbt8")

swades = media.Movie("Swades", "Soulsearching India trip for a NASA NRI Engineer"
          , "http://www.impawards.com/intl/india/2004/posters/swades.jpg"
          , "https://www.youtube.com/watch?v=y95DpoSP7i0")

movies = [dangal, the_departed, three_idiots, predestination, finding_nemo, swades]
fresh_tomatoes.open_movies_page(movies)
