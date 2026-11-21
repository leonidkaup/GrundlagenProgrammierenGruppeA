#Leonid Kaup
def search_by_title(filmlist, title):
    result = []
    for film in filmlist:
        film_title = film.get("title", film.get("titel", ""))
        if title.lower().strip() in film_title.lower().strip():
            result.append(film)
    return result

#Leonid Kaup
def search_by_genre(filmlist, genre):
    result = []
    for film in filmlist:
        if film["genre"].lower().strip() == genre.lower().strip():
            result.append(film)
    return result

#Leonid Kaup
def search_by_actors(filmlist, actors):
    result = []
    for actor in actors:
        for film in filmlist:
            for filmactor in film["actors"]:
                if actor.lower().strip() in filmactor.lower().strip():
                    result.append(film)
    return result

#Leonid Kaup
def sort_list_by_rating(filmlist):
    sortedList= sorted(filmlist, key=rating, reverse=True)
    return sortedList

#Leonid Kaup
def rating(film):
    return film["rating"] if film["rating"] is not None else 0

#Leonid Kaup
def top_films(filmlist, top_number):
    sorted_list = sort_list_by_rating(filmlist)
    if top_number > len(sorted_list):
        top_number = len(sorted_list)
    return sorted_list[:top_number]

#Leonid Kaup
def flop_films(filmlist, flop_number):
    sorted_list = sort_list_by_rating(filmlist)
    if flop_number > len(sorted_list):
        flop_number = len(sorted_list)
    if flop_number <= 0:
        return []
    return sorted_list[-flop_number:]

#Leonid Kaup
def unrated_films(filmlist):
    result = []
    for film in filmlist:
        if film["rating"] == None:
            result.append(film)
    return result

#Leonid Kaup
def _read_result_count(prompt):
    while True:
        count_text = input(
            f"\n{prompt}, or enter B to go back: "
        ).strip()
        if count_text.lower() == "b":
            return None
        try:
            count = int(count_text)
            if count < 1:
                raise ValueError
            return count
        except ValueError:
            print("Please enter a whole number greater than 0.")

#Leonid Kaup
def _print_search_results(films):
    if not films:
        print("No matching movies found.")
        return

    print("\nMovies:")
    for film in films:
        title = film.get("title", film.get("titel", "Unknown title"))
        rating_value = film.get("rating")
        if rating_value is None:
            rating_value = "Not rated"
        print(f"- {title} (Rating: {rating_value})")
