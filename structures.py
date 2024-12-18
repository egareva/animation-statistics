import dataclasses
from typing import Optional


@dataclasses.dataclass
class AnimationInfo:
    name: str
    year: str | None
    index: int
    rating: int

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other: 'AnimationInfo') -> bool:
        return self.name == other.name and self.year == other.year


@dataclasses.dataclass
class ChannelData:
    title: str
    link: str
    votes: list[AnimationInfo]


@dataclasses.dataclass
class AnimationInfoStatistics:
    name: str
    total_rating: int
    total_votes: int
    rating_dict: dict[int, int]
    places_dict: dict[int, int]
    final_place: int | None = None
    average_vote_place: float | None = None


@dataclasses.dataclass
class DatabaseRow:
    title: str
    year: str


@dataclasses.dataclass
class AnimationInfoStatistics:
    title: str
    total_rating: int
    total_votes: int
    rating_dict: dict[int, int]
    places_dict: dict[int, int]
    final_place: Optional[int] = None
    average_vote_place: Optional[float] = None