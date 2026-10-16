from dataclasses import dataclass
from typing import Any
from utils.helper import validate_date, validate_list


@dataclass
class Film:
    title: str
    date_of_release: str
    genre: str
    rating: int
    description: str
    actors: list[str]
    watch_date: str

    def to_dict(self) -> dict[str, Any]:
        return {
            "titel": self.title,
            "dateOfRelease": self.date_of_release,
            "genre": self.genre,
            "rating": self.rating,
            "description": self.description,
            "actors": self.actors,
            "watchdate": self.watch_date,
        }

    # validation for conversions from dict to Film
    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Film":
        # check if correct keys are present
        if set(data.keys()) != {"titel","dateOfRelease","genre","rating","description","actors","watchdate"}:
            raise ValueError(
                f"Validation failed: keys are {set(data.keys())}; expected "
                "titel, dateOfRelease, genre, rating, description, actors, watchdate"
            )
        
        # check that values have correct datatype and required strings are not empty
        # title should not be empty
        if type(data["titel"]) != str or len(data["titel"]) < 1:
            raise ValueError(
                f"Validation failed: titel is {data['titel']}; "
                "expected a non-empty string"
            )
        # dateOfRelease should not be empty
        if type(data["dateOfRelease"]) != str or len(data["dateOfRelease"]) < 1 or not validate_date(data["dateOfRelease"]):
            raise ValueError(
                f"Validation failed: dateOfRelease is {data['dateOfRelease']}; "
                'expected a valid date in "dd.mm.yyyy" format'
            )
        # genre should not be empty
        if type(data["genre"]) != str or len(data["genre"]) < 1:
            raise ValueError(
                f"Validation failed: genre is {data['genre']}; "
                "expected a non-empty string"
            )
        # rating is not mandatory in time of import
        if data["rating"] is not None and ( not isinstance(data["rating"], int) or isinstance(data["rating"], bool) or not 1 <= data["rating"] <= 10):
            raise ValueError(
                f"Validation failed: rating is {data['rating']}"
                f"(type: {type(data['rating'])}); "
                "expected an integer or null"
            )
        # description can be empty
        if type(data["description"]) != str:
            raise ValueError(
                f"Validation failed: description is {data['description']}; "
                "expected a string"
            )
        if not validate_list(data["actors"],str):
            raise ValueError(
                f"Validation failed: actors is {data['actors']} "
                f"(type: {type(data['actors'])}); "
                "expected a list of actor names as str"
            )
        if type(data["watchdate"]) != str or (len(data["watchdate"]) > 0 and not validate_date(data["watchdate"])):
            raise ValueError(
                f"Validation failed: watchdate is {data['watchdate']}; "
                'expected an empty string or a valid date in "dd.mm.yyyy" format'
            )

        return cls(
            title=data["titel"],
            date_of_release=data["dateOfRelease"],
            genre=data["genre"],
            rating=data["rating"],
            description=data["description"],
            actors=data["actors"],
            watch_date=data["watchdate"],
        )
