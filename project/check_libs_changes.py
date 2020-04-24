import os

from routes import FILMS
from database import MediaDB

database = MediaDB()
videos_in_db = database.get_videos()

videos_in_folder = os.listdir(path=FILMS)

# print(videos_in_folder)
# print(videos_in_db)

a = set(['dfsffsd.465464', 'dfdfsdff.343', 'dfffff.333'])
b = set(['dfsffsd.465464', 'dfdfsdff.343'])
c = a - b
print(c)

# import hashlib
#
# file1 = open('file1.avi', 'r').read()
# file2 = open('file2.avi', 'r').read()
#
# if hashlib.sha512(file1).hexdigest() == hashlib.sha512(file2).hexdigest():
#      print 'They are the same'
# else:
#      print 'They are different'

# for video in videos_in_folder
print(os.stat(FILMS+'/'+'Who Framed Roger Rabbit/1.bmp'))
# os.stat_result(st_mode=33206, st_ino=120328, st_dev=3895396254, st_nlink=1, st_uid=0, st_gid=0, st_size=0, st_atime=1587767051, st_mtime=1587767051, st_ctime=1587767051)
# os.stat_result(st_mode=33206, st_ino=120328, st_dev=3895396254, st_nlink=1, st_uid=0, st_gid=0, st_size=25165878, st_atime=1587767051, st_mtime=1587767104, st_ctime=1587767051)
