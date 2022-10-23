import sys
from pathlib import Path

JPEG_IMAGES = []
JPG_IMAGES = []
PNG_IMAGES = []
SVG_IMAGES = []

MP3_AUDIO = []
OGG_AUDIO = []
WAV_AUDIO = []
AMR_AUDIO = []

AVI_VIDEO = []
MP4_VIDEO = []
MOV_VIDEO = []
MKV_VIDEO = []

DOC_DOCUMENTS = []
DOCX_DOCUMENTS = []
TXT_DOCUMENTS = []
PDF_DOCUMENTS = []
XLSX_DOCUMENTS = []
PPTX_DOCUMENTS = []

MY_OTHER = []

ZIP_ARCHIVES = []
GZ_ARCHIVES = []
TAR_ARCHIVES = []

REGISTER_EXTENSIONS = {
    'JPEG': JPEG_IMAGES,
    'PNG': PNG_IMAGES,
    'JPG': JPG_IMAGES,
    'SVG': SVG_IMAGES,
    'MP3': MP3_AUDIO,
    'OGG': OGG_AUDIO,
    'WAV': WAV_AUDIO,
    'AMR': AMR_AUDIO,
    'AVI': AVI_VIDEO,
    'MP4': MP4_VIDEO,
    'MOV': MOV_VIDEO,
    'MKV': MKV_VIDEO,
    'DOC': DOC_DOCUMENTS,
    'DOCX': DOCX_DOCUMENTS,
    'TXT': TXT_DOCUMENTS,
    'PDF': PDF_DOCUMENTS,
    'XLSX': XLSX_DOCUMENTS,
    'PPTX': PPTX_DOCUMENTS,
    'ZIP': ZIP_ARCHIVES,
    'GZ': GZ_ARCHIVES,
    'TAR': TAR_ARCHIVES
}

FOLDERS = []
EXTENSIONS = set()
UNKNOWN = set()


def get_extension(filename: str) -> str:
    # перетворюємо розширення файлу на назву папки .jpg -> JPG
    return Path(filename).suffix[1:].upper()


def scan(folder: Path) -> None:
    for item in folder.iterdir():
        # Якщо це папка то додаємо її зі списку FOLDERS і переходимо до наступного елемента папки
        if item.is_dir():
            # перевіряємо, щоб папка не була тією, в яку ми складаємо вже файли.
            if item.name not in ('archives', 'video', 'audio', 'documents', 'images', 'MY_OTHER'):
                FOLDERS.append(item)
                # скануємо цю вкладену папку - рекурсія
                scan(item)
            # перейти до наступного елемента в сканованій папці
            continue

        # Робота з файлом
        ext = get_extension(item.name)  # взяти розширення
        fullname = folder / item.name  # взяти повний шлях до файлу (folder / item.name)
        if not ext:  # якщо файл не має розширення додати до невідомих
            MY_OTHER.append(fullname) # fullname
        else:
            try:
                # взяти список куди покласти повний шлях до файлу
                container = REGISTER_EXTENSIONS[ext]
                EXTENSIONS.add(ext)
                container.append(fullname) #fullname
            except KeyError:
                # Якщо ми не реєстрували розширення у REGISTER_EXTENSIONS, то додати до іншого
                UNKNOWN.add(ext)
                MY_OTHER.append(fullname) #fullname


if __name__ == '__main__':

    folder_for_scan = sys.argv[1]

    print(f'Start in folder {folder_for_scan}')

    scan(Path(folder_for_scan))

    # print(f'Images jpeg: {JPEG_IMAGES}')
    # print(f'Images jpg: {JPG_IMAGES}')
    # print(f'Images svg: {SVG_IMAGES}')
    # print(f'Images png: {PNG_IMAGES}')
    #
    # print(f'Audio mp3: {MP3_AUDIO}')
    # print(f'Audio ogg: {OGG_AUDIO}')
    # print(f'Audio wav: {WAV_AUDIO}')
    # print(f'Audio amr: {AMR_AUDIO}')
    #
    # print(f'Video avi: {AVI_VIDEO}')
    # print(f'Video mp4: {MP4_VIDEO}')
    # print(f'Video mov: {MOV_VIDEO}')
    # print(f'Video mkv: {MKV_VIDEO}')
    #
    # print(f'Dokument doc: {DOC_DOCUMENTS}')
    # print(f'Dokument docx: {DOCX_DOCUMENTS}')
    # print(f'Dokument txt: {TXT_DOCUMENTS}')
    # print(f'Dokument pdf: {PDF_DOCUMENTS}')
    # print(f'Dokument xlsx: {XLSX_DOCUMENTS}')
    # print(f'Dokument pptx: {PPTX_DOCUMENTS}')
    #
    # print(f'Archives zip: {ZIP_ARCHIVES}')
    # print(f'Archives gz: {GZ_ARCHIVES}')
    # print(f'Archives tar: {TAR_ARCHIVES}')
    #
    # print(f'Types of files in folder: {EXTENSIONS}')
    # print(f'Unknown files of types: {UNKNOWN}')
    #
    # print(f'Others file: {MY_OTHER}')
    #
    # print(f"Folders: {FOLDERS[::-1]}")


    result = f'''Images jpeg: {JPEG_IMAGES}'
        \n\nImages jpg: {JPG_IMAGES}
        \n\nImages svg: {SVG_IMAGES}
        \n\nImages png: {PNG_IMAGES}
        \n\nAudio mp3: {MP3_AUDIO}
        \n\nAudio ogg: {OGG_AUDIO}
        \n\nAudio wav: {WAV_AUDIO}
        \n\nAudio amr: {AMR_AUDIO}
        \n\nVideo avi: {AVI_VIDEO}
        \n\nVideo mp4: {MP4_VIDEO}
        \n\nVideo mov: {MOV_VIDEO}
        \n\nVideo mkv: {MKV_VIDEO}
        \n\nDokument doc: {DOC_DOCUMENTS}
        \n\nDokument docx: {DOCX_DOCUMENTS}
        \n\nDokument txt: {TXT_DOCUMENTS}
        \n\nDokument pdf: {PDF_DOCUMENTS}
        \n\nDokument xlsx: {XLSX_DOCUMENTS}
        \n\nDokument pptx: {PPTX_DOCUMENTS}
        \n\nArchives zip: {ZIP_ARCHIVES}
        \n\nArchives gz: {GZ_ARCHIVES}
        \n\nArchives tar: {TAR_ARCHIVES}
        \n\nTypes of files in folder: {EXTENSIONS}
        \n\nUnknown files of types: {UNKNOWN}
        \n\nOthers file: {MY_OTHER}
        \n\nFolders: {FOLDERS[::-1]}'''
    print(result)

# TODO: запускаємо:  python3 file_parser.py `назва_папки_для_сортування`