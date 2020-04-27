import os

from routes import FILMS
from db_exchange import MediaDB

database = MediaDB()
videos_in_db = database.get_videos()
videos_in_folder = os.listdir(path=FILMS)


def check_new_videos():
    new_videos = set(videos_in_folder) - set(videos_in_db.values())
    if new_videos:
        for video in new_videos:
            database.insert_row({
                'name': video,
                'categories_id': '1'
            })


if __name__ == "__main__":
    check_new_videos()
