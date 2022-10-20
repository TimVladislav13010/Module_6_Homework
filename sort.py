import os
import re
import sys


def sorter(path=sys.argv[1]):
    for i in os.listdir(path): #iterator po papkah
        # print(i)
        if i.endswith(".jpg") \
                or i.endswith(".jpeg") \
                or i.endswith(".png") \
                or i.endswith(".svg"):
            print(f"this is foto fille {i}")
        if i.endswith(".avi") \
                or i.endswith(".mp4") \
                or i.endswith(".mov") \
                or i.endswith(".mkv"):
            print(f"this is video fille {i}")
        if i.endswith(".doc")\
                or i.endswith(".docx") \
                or i.endswith(".txt") \
                or i.endswith(".pdf") \
                or i.endswith(".xlsx") \
                or i.endswith(".pptx"):
            print(f"this is documents fille {i}")
        if i.endswith(".mp3") \
                or i.endswith(".ogg") \
                or i.endswith(".wav") \
                or i.endswith(".amr"):
            print(f"this is musiс fille {i}")
        if i.endswith(".zip") \
                or i.endswith(".gz") \
                or i.endswith(".tar"):
            print(f"this is archives fille {i}")
        elif os.path.isfile(os.path.join(path, i)):
            print(f"this is uknown fille {i}")
        if os.path.isdir(os.path.join(path, i)): #yakscho papka to zahodumo v nei
            if i == "audio" or i =="video" or i == "archives" or i == "documents" or i =="images":
                continue #perevirka na papku
            sorter(os.path.join(path, i)) #recursuvno vuklukaemo funk


sorter()
