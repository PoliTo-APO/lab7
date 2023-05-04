from typing import List, Optional


class MediaContent:
    def __init__(self, title: str, year: int) -> None:
        self._title = title
        self._year = year
        self._watchers = set()
        self._ratings = {}
        self._previous = []

    def get_title(self) -> str:
        return self._title

    def get_year(self) -> int:
        return self._year

    def get_content_type(self) -> str:
        raise NotImplementedError

    def __repr__(self) -> str:
        pass

    def add_watcher(self, user):
        self._watchers.add(user)

    def get_watchers(self):
        return self._watchers

    def add_rating(self, user_name, rating):
        self._ratings[user_name] = rating

    def get_ratings(self):
        return self._ratings

    def get_avg_rating(self):
        raise NotImplementedError

    def add_previous(self, content):
        self._previous.append(content)

    def get_previous(self):
        return self._previous


class Movie(MediaContent):
    def __init__(self, title, year, director, duration):
        super().__init__(title, year)
        self._director = director
        self._duration = duration

    def get_content_type(self):
        return "movie"

    def __repr__(self):
        return "{},{},{},{}".format(self._title, self._year, self._director, self._duration)

    def get_avg_rating(self):
        ratings = sorted(self.get_ratings().values())
        if len(ratings) > 2:
            ratings = ratings[1:-1]
        return sum(ratings)/len(ratings)


class TVShow(MediaContent):
    def __init__(self, title, year, num_seasons, num_episodes):
        super().__init__(title, year)
        self._num_seasons = num_seasons
        self._num_episodes = num_episodes

    def get_content_type(self):
        return "tv show"

    def __repr__(self):
        return "{},{},{},{}".format(self._title, self._year, self._num_seasons, self._num_episodes)

    def get_avg_rating(self):
        ratings = list(self.get_ratings().values())
        ratings += [5]*10
        return sum(ratings)/len(ratings)


class User:
    def __init__(self, name, age):
        self._name = name
        self._age = age
        self._watched_contents = []
        self._ratings = {}

    def get_name(self):
        return self._name
    
    def add_watched_content(self, content):
        self._watched_contents.append(content)

    def get_watched_contents(self):
        return self._watched_contents

    def add_rating(self, title, rating):
        self._ratings[title] = rating

    def get_ratings(self):
        return self._ratings


class StreamingService:
    def __init__(self):
        self._contents = {}
        self._users = {}
        self._ratings = {}

    # R1
    def add_movie(self, title: str, year: int, director: str, duration: int) -> None:
        self._contents[title] = Movie(title, year, director, duration)
    
    def add_tv_show(self, title: str, year: int, num_seasons: int, num_episodes: int) -> None:
        self._contents[title] = TVShow(title, year, num_seasons, num_episodes)

    def get_media_content(self, title: str) -> MediaContent:
        return self._contents[title]

    # R2
    def add_user(self, name: str, age: int) -> None:
        self._users[name] = User(name, age)

    def watch(self, user_name: str, title: str) -> None:
        content = self._contents[title]
        user = self._users[user_name]
        content.add_watcher(user)
        user.add_watched_content(content)
    
    def get_watched_by_user(self, user_name: str, min_year: Optional[int] = None) -> List[MediaContent]:
        return [content for content in self._users[user_name].get_watched_contents() if min_year is None or content.get_year() > min_year]

    def get_watchers_of_content(self, title: str) -> List[str]:
        return [user.get_name() for user in self._contents[title].get_watchers()]

    # R3
    def add_rating(self, user_name: str, title: str, rating: int) -> None:
        user = self._users[user_name]
        content = self._contents[title]
        user.add_rating(title, rating)
        content.add_rating(user_name, rating)

    def get_avg_content_rating(self, title: str) -> float:
        return self._contents[title].get_avg_rating()

    def get_avg_user_rating(self, user_name: str) -> float:
        ratings = self._users[user_name].get_ratings().values()
        return sum(ratings)/len(ratings)

    # R4
    def get_recommendations(self, user_name: str) -> List[str]:
        recommendations = set()
        watched_contents = self._users[user_name].get_watched_contents()
        for content in watched_contents:
            for watcher in content.get_watchers():
                for new_content in watcher.get_watched_contents():
                    recommendations.add(new_content.get_title())

        already_watched = {content.get_title() for content in watched_contents}
        return list(recommendations - already_watched)

    # R5
    def set_previous_content(self, title: str, previous_title: str) -> None:
        content = self._contents[title]
        previous = self._contents[previous_title]
        content.add_previous(previous)

    def get_watch_list(self, title: str) -> list[str]:
        content = self._contents[title]
        watch_list = []
        self._explore_previous(content, watch_list)
        return watch_list

    def _explore_previous(self, content: MediaContent, watch_list: list[str]) -> None:
        for previous in content.get_previous():
            self._explore_previous(previous, watch_list)
        watch_list.append(content.get_title())



            
            







