import os
while os.path.exists("my_second_novel.txt"):
    print ("True")
    break #break will exit the for or while loop after the first iteration of the loop
else:
    print ("False")
