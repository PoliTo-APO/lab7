from typing import List, Optional


class MediaContent:
    def __init__(self, title: str, year: int) -> None:
        pass

    def get_title(self) -> str:
        pass

    def get_year(self) -> int:
        pass

    def get_content_type(self) -> str:
        raise NotImplementedError

    def __repr__(self) -> str:
        pass


class StreamingService:
    def __init__(self):
        pass

    # R1
    def add_movie(self, title: str, year: int, director: str, duration: int) -> None:
        pass
    
    def add_tv_show(self, title: str, year: int, num_seasons: int, num_episodes: int) -> None:
        pass

    def get_media_content(self, title: str) -> MediaContent:
        pass

    # R2
    def add_user(self, name: str, age: int) -> None:
        pass

    def watch(self, user_name: str, title: str) -> None:
        pass
    
    def get_watched_by_user(self, user_name: str, min_year: Optional[int] = None) -> List[MediaContent]:
        pass

    def get_watchers_of_content(self, title: str) -> List[str]:
        pass

    # R3
    def add_rating(self, user_name: str, title: str, rating: int) -> None:
        pass

    def get_avg_content_rating(self, title: str) -> float:
        pass

    def get_avg_user_rating(self, user_name: str) -> float:
        pass

    # R4
    def get_recommendations(self, user_name: str) -> List[str]:
        pass

    # R5
    def set_previous_content(self, title: str, previous_title: str) -> None:
        pass

    def get_watch_list(self, title: str) -> list[str]:
        pass
    