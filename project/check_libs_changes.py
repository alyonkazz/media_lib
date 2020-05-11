import os

from db_exchange import MediaDB

database = MediaDB()
folder_list = database.get_video_path_folders()


def check_new_videos():
    for i in range(len(folder_list)):
        videos_in_folder = os.listdir(path=folder_list[i])
        videos_in_db = database.get_videos_by_category(i+1)
        new_videos = set(videos_in_folder) - set(videos_in_db.values())
        if new_videos:
            for video in new_videos:
                database.insert_row({
                    'name': video,
                    'categories_id': str(i+1)
                })


if __name__ == "__main__":
    check_new_videos()
