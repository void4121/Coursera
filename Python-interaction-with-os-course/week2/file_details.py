import os
import datetime

print(os.path.getsize("my_second_novel.txt"))

timestamp = os.path.getmtime("my_second_novel.txt")
print(datetime.datetime.fromtimestamp(timestamp))

print(os.path.abspath("notes.txt"))