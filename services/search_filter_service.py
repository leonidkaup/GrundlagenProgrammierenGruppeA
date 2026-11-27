import json

from storage.store_service import get_all_persisted_films
from utils.sort_filter_helper import (
    search_by_title,
    search_by_actors,
    sort_list_by_rating,
    top_films,
    flop_films,
    _read_result_count,
    _print_search_results,
    unrated_films,
)

#Leonid Kaup
def search_filter_sort_movie():
    while True:
        action = input(
            "\nHow would you like to browse your movies?\n"
            "  1: Search by title or actor\n"
            "  2: Show a list sorted by rating\n"
            "  3: Show the top-rated movies\n"
            "  4: Show the lowest-rated movies\n"
            "  5: Show unrated movies\n"
            "  B: Back to menu\n"
            "\nPlease enter 1, 2, 3, 4, 5, or B: "
        ).strip().lower()

        if action == "1":
            search_movies()
        elif action == "2":
            sort_movies_by_rating()
        elif action == "3":
            show_top_movies()
        elif action == "4":
            show_flop_movies()
        elif action == "5":
            show_unrated_movies()
        elif action == "b":
            return
        else:
            print("Please enter 1, 2, 3, 4, 5, or B.")

#Leonid Kaup
def search_movies():
    while True:
        filter_action = input(
            "\nWhat would you like to search by?\n"
            "  A - Actor\n"
            "  T - Movie title\n"
            "  B - Back to menu\n"
            "\nPlease enter A, T, or B: "
        ).strip().lower()

        if filter_action == "b":
            return
        elif filter_action == "a":
            search_movies_by_actor()
        elif filter_action == "t":
            search_movies_by_title()
        else:
            print("Please enter A, T, or B.")

#Leonid Kaup
def search_movies_by_actor():
    while True:
        try:
            actor_names = input(
                "\nEnter actor names separated by commas, or B to go back: "
            ).strip()
            if actor_names.lower() == "b":
                return
            if not actor_names:
                raise ValueError("Please enter at least one actor name.")

            actors = [
                actor.strip()
                for actor in actor_names.split(",")
                if actor.strip()
            ]

            films = get_all_persisted_films()
            results = search_by_actors(films, actors)
            _print_search_results(results)
            return
        except (json.JSONDecodeError, KeyError, TypeError, ValueError) as error:
            print(f"Search failed: {error}")

#Leonid Kaup
def search_movies_by_title():
    while True:
        try:
            title = input(
                "\nEnter the movie title, or B to go back: "
            ).strip()
            if title.lower() == "b":
                return
            if not title:
                raise ValueError("Please enter a movie title.")

            films = get_all_persisted_films()
            results = search_by_title(films, title)
            _print_search_results(results)
            return
        except (json.JSONDecodeError, KeyError, TypeError, ValueError) as error:
            print(f"Search failed: {error}")

#Leonid Kaup
def sort_movies_by_rating():
    try:
        films = get_all_persisted_films()
        _print_search_results(sort_list_by_rating(films))
    except (json.JSONDecodeError, KeyError, TypeError, ValueError) as error:
        print(f"Sorting failed: {error}")

#Leonid Kaup
def show_top_movies():
    try:
        top_number = _read_result_count("Enter the number of top-rated movies")
        if top_number is None:
            return
        films = get_all_persisted_films()
        _print_search_results(top_films(films, top_number))
    except (json.JSONDecodeError, KeyError, TypeError, ValueError) as error:
        print(f"Could not get the top-rated movies: {error}")

#Leonid Kaup
def show_flop_movies():
    try:
        flop_number = _read_result_count("Enter the number of lowest-rated movies")
        if flop_number is None:
            return
        films = get_all_persisted_films()
        _print_search_results(flop_films(films, flop_number))
    except (json.JSONDecodeError, KeyError, TypeError, ValueError) as error:
        print(f"Could not get the lowest-rated movies: {error}")

#Leonid Kaup
def show_unrated_movies():
    try:
        films = get_all_persisted_films()
        _print_search_results(unrated_films(films))
    except (json.JSONDecodeError, KeyError, TypeError, ValueError) as error:
        print(f"Could not get the unrated movies: {error}")
