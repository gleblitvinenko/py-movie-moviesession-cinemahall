from django.db.models import QuerySet

from datetime import datetime

from typing import Optional

from db.models import MovieSession


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int
) -> MovieSession:
    return MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id
    )


def get_movies_sessions(
        session_date: Optional = None
) -> QuerySet[MovieSession]:
    queryset = MovieSession.objects.all()

    if session_date:
        queryset = queryset.filter(show_time__date=session_date)

    return queryset


def get_movie_session_by_id(
        movie_session_id: int
) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: Optional[datetime] = None,
        movie_id: Optional[int] = None,
        cinema_hall_id: Optional[int] = None
) -> MovieSession:
    updated_movie = MovieSession.objects.filter(id=session_id)

    if show_time:
        updated_movie.update(show_time=show_time)

    if movie_id:
        updated_movie.update(movie=movie_id)

    if cinema_hall_id:
        updated_movie.update(cinema_hall_id=cinema_hall_id)

    return updated_movie


def delete_movie_session_by_id(
        session_id: int
) -> None:
    get_movie_session_by_id(session_id).delete()