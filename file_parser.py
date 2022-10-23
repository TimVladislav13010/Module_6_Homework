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

JPEG_IMAGES_NAME = []
JPG_IMAGES_NAME = []
PNG_IMAGES_NAME = []
SVG_IMAGES_NAME = []

MP3_AUDIO_NAME = []
OGG_AUDIO_NAME = []
WAV_AUDIO_NAME = []
AMR_AUDIO_NAME = []

AVI_VIDEO_NAME = []
MP4_VIDEO_NAME = []
MOV_VIDEO_NAME = []
MKV_VIDEO_NAME = []

DOC_DOCUMENTS_NAME = []
DOCX_DOCUMENTS_NAME = []
TXT_DOCUMENTS_NAME = []
PDF_DOCUMENTS_NAME = []
XLSX_DOCUMENTS_NAME = []
PPTX_DOCUMENTS_NAME = []

MY_OTHER_NAME = []

ZIP_ARCHIVES_NAME = []
GZ_ARCHIVES_NAME = []
TAR_ARCHIVES_NAME = []

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

REGISTER_EXTENSIONS_NAME = {
    'JPEG': JPEG_IMAGES_NAME,
    'PNG': PNG_IMAGES_NAME,
    'JPG': JPG_IMAGES_NAME,
    'SVG': SVG_IMAGES_NAME,
    'MP3': MP3_AUDIO_NAME,
    'OGG': OGG_AUDIO_NAME,
    'WAV': WAV_AUDIO_NAME,
    'AMR': AMR_AUDIO_NAME,
    'AVI': AVI_VIDEO_NAME,
    'MP4': MP4_VIDEO_NAME,
    'MOV': MOV_VIDEO_NAME,
    'MKV': MKV_VIDEO_NAME,
    'DOC': DOC_DOCUMENTS_NAME,
    'DOCX': DOCX_DOCUMENTS_NAME,
    'TXT': TXT_DOCUMENTS_NAME,
    'PDF': PDF_DOCUMENTS_NAME,
    'XLSX': XLSX_DOCUMENTS_NAME,
    'PPTX': PPTX_DOCUMENTS_NAME,
    'ZIP': ZIP_ARCHIVES_NAME,
    'GZ': GZ_ARCHIVES_NAME,
    'TAR': TAR_ARCHIVES_NAME
}

FOLDERS = []
FOLDERS_NAME = []
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
                FOLDERS_NAME.append(item.name)
                # скануємо цю вкладену папку - рекурсія
                scan(item)
            # перейти до наступного елемента в сканованій папці
            continue

        # Робота з файлом
        ext = get_extension(item.name)  # взяти розширення
        fullname = folder / item.name  # взяти повний шлях до файлу (folder / item.name)
        if not ext:  # якщо файл не має розширення додати до невідомих
            MY_OTHER.append(fullname)  # fullname
            MY_OTHER_NAME.append(item.name)
        else:
            try:
                # взяти список куди покласти повний шлях до файлу
                container = REGISTER_EXTENSIONS[ext]
                container_name = REGISTER_EXTENSIONS_NAME[ext]
                EXTENSIONS.add(ext)
                container.append(fullname)  # fullname
                container_name.append(item.name)
            except KeyError:
                # Якщо ми не реєстрували розширення у REGISTER_EXTENSIONS, то додати до іншого
                UNKNOWN.add(ext)
                MY_OTHER.append(fullname)  # fullname
                MY_OTHER_NAME.append(item.name)

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

    result = f'''Images jpeg: {[JPEG_IMAGES_NAME]}
        \n\nImages jpg: {JPG_IMAGES_NAME}
        \n\nImages svg: {SVG_IMAGES_NAME}
        \n\nImages png: {PNG_IMAGES_NAME}
        \n\nAudio mp3: {MP3_AUDIO_NAME}
        \n\nAudio ogg: {OGG_AUDIO_NAME}
        \n\nAudio wav: {WAV_AUDIO_NAME}
        \n\nAudio amr: {AMR_AUDIO_NAME}
        \n\nVideo avi: {AVI_VIDEO_NAME}
        \n\nVideo mp4: {MP4_VIDEO_NAME}
        \n\nVideo mov: {MOV_VIDEO_NAME}
        \n\nVideo mkv: {MKV_VIDEO_NAME}
        \n\nDokument doc: {DOC_DOCUMENTS_NAME}
        \n\nDokument docx: {DOCX_DOCUMENTS_NAME}
        \n\nDokument txt: {TXT_DOCUMENTS_NAME}
        \n\nDokument pdf: {PDF_DOCUMENTS_NAME}
        \n\nDokument xlsx: {XLSX_DOCUMENTS_NAME}
        \n\nDokument pptx: {PPTX_DOCUMENTS_NAME}
        \n\nArchives zip: {ZIP_ARCHIVES_NAME}
        \n\nArchives gz: {GZ_ARCHIVES_NAME}
        \n\nArchives tar: {TAR_ARCHIVES_NAME}
        \n\nTypes of files in folder: {EXTENSIONS}
        \n\nUnknown files of types: {UNKNOWN}
        \n\nOthers file: {MY_OTHER_NAME}
        \n\nFolders: {FOLDERS_NAME[::-1]}'''

    print(result)


# TODO: запускаємо:  python3 file_parser.py `назва_папки_для_сортування`
