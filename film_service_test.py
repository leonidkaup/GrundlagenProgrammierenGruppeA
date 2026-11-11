from services.film_service import (
    search_by_title,
    search_by_genre,
    search_by_actors,
    sort_list_by_rating,
    top_films,
    flop_films
)

# Testdaten
movies = [
    {
        "title": "The Matrix",
        "dateOfRelease": "31.03.1999",
        "genre": "Science Fiction",
        "rating": 9,
        "description": "A hacker discovers the truth about reality.",
        "actors": ["Keanu Reeves", "Laurence Fishburne"],
        "watchdate": "10.10.2026"
    },
    {
        "title": "Gladiator",
        "dateOfRelease": "05.05.2000",
        "genre": "Action",
        "rating": 8,
        "description": "A Roman general becomes a gladiator.",
        "actors": ["Russell Crowe", "Joaquin Phoenix"],
        "watchdate": "11.10.2026"
    }
]


# Test 1: Suche nach Titel
result = search_by_title(movies, "the matrix")
assert len(result) == 1
assert result[0]["title"] == "The Matrix"
print("Test 1: Titelsuche bestanden")


# Test 2: Suche nach Genre
result = search_by_genre(movies, "action")
assert len(result) == 1
assert result[0]["title"] == "Gladiator"
print("Test 2: Genresuche bestanden")


# Test 3: Suche nach Schauspieler
result = search_by_actors(movies, ["Keanu Reeves"])
assert len(result) == 1
assert result[0]["title"] == "The Matrix"
print("Test 3: Schauspielersuche bestanden")


# Test 4: Sortierung nach Rating
result = sort_list_by_rating(movies)
assert result[0]["rating"] == 9
assert result[1]["rating"] == 8
print("Test 4: Rating-Sortierung bestanden")


# Test 5: Top 1 Film
result = top_films(movies, 1)
assert len(result) == 1
assert result[0]["title"] == "The Matrix"
print("Test 5: Top-Filme bestanden")


# Test 6: Flop 1 Film
result = flop_films(movies, 1)
assert len(result) == 1
assert result[0]["title"] == "Gladiator"
print("Test 6: Flop-Filme bestanden")


# Test 7: Nicht vorhandener Titel
result = search_by_title(movies, "Titanic")
assert result == []
print("Test 7: Unbekannter Titel bestanden")


# Test 8: Leere Filmliste
result = top_films([], 5)
assert result == []
print("Test 8: Leere Filmliste bestanden")


# Test 9: Mehr Filme anfordern als vorhanden
result = top_films(movies, 10)
assert len(result) == 2
print("Test 9: Top 10 bei nur 2 Filmen bestanden")


# Test 10: Originalreihenfolge bleibt unverändert
assert movies[0]["title"] == "The Matrix"
assert movies[1]["title"] == "Gladiator"
print("Test 10: Originalreihenfolge unverändert bestanden")


print("\nAlle 10 Tests bestanden!")
