from dataclasses import dataclass
from typing import Any


@dataclass
class Film:
    title: str
    date_of_release: str
    genre: str
    rating: float
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

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Film":
        return cls(
            title=data["titel"],
            date_of_release=data["dateOfRelease"],
            genre=data["genre"],
            rating=data["rating"],
            description=data["description"],
            actors=data["actors"],
            watch_date=data["watchdate"],
        )
