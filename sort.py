import os
import re
import sys


def sorter(path=sys.argv[1]):

    for i in os.listdir(path): #iterator po papkah
        print(i)
        if i.endswith(".jpg") \
                or i.endswith(".jpeg") \
                or i.endswith(".png") \
                or i.endswith(".svg"):
            print(f"this is photo fille {i}")
            lists_photo.append(i)
        elif i.endswith(".avi") \
                or i.endswith(".mp4") \
                or i.endswith(".mov") \
                or i.endswith(".mkv"):
            print(f"this is video fille {i}")
            lists_video.append(i)
        elif i.endswith(".doc")\
                or i.endswith(".docx") \
                or i.endswith(".txt") \
                or i.endswith(".pdf") \
                or i.endswith(".xlsx") \
                or i.endswith(".pptx"):
            print(f"this is documents fille {i}")
            lists_documents.append(i)
        elif i.endswith(".mp3") \
                or i.endswith(".ogg") \
                or i.endswith(".wav") \
                or i.endswith(".amr"):
            print(f"this is musiс fille {i}")
            lists_music.append(i)
        elif i.endswith(".zip") \
                or i.endswith(".gz") \
                or i.endswith(".tar"):
            print(f"this is archives fille {i}")
            lists_archive.append(i)
        elif os.path.isfile(os.path.join(path, i)):
            print(f"this is uknown fille {i}")
            lists_uknown.append(i)
        if os.path.isdir(os.path.join(path, i)): #yakscho papka to zahodumo v nei
            if i == "audio" or i =="video" or i == "archives" or i == "documents" or i =="images":
                continue #perevirka na papku
            sorter(os.path.join(path, i)) #recursuvno vuklukaemo funk
    return lists_music, lists_photo, lists_video, lists_archive, lists_documents, lists_uknown


lists_music = []
lists_archive = []
lists_video = []
lists_documents = []
lists_photo = []
lists_uknown = []


a = sorter()
print(a)