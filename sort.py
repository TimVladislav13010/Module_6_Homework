from pathlib import Path
from normalize import normalize
import sys
import time

#Списки файлів


text_file = []
audio_file = []
video_file = []
photo_file = []
archives_file = []
others_file = []
folders = []
set_suffix_known = set()
set_suffix_unknown = set()


def sorter(path): # функція сортування файлів

    for i in path.iterdir(): # ітерація по файлах та папках за вказаним шляхом

        if i.is_dir(): # якщо папка то заходимо в неї рекурсивно викликаємо функцію
            folders.append(i.name)
            sorter(path / i)

        if i.is_file(): # якщо файл перевіряємо розширення та додаємо інформацію до списків
            path_file = path / i
            format_files = path_file.suffix

            if format_files == ".txt" \
                    or format_files == ".doc" \
                    or format_files == ".docx" \
                    or format_files == ".pdf" \
                    or format_files == ".pptx" \
                    or format_files == ".xlsx": # перевірка текстових файлів

                text_file.append(path_file.name)
                set_suffix_known.add(path_file.suffix)
                move_file(path_file, PATH / "documents")

            elif format_files == ".jpeg" \
                    or format_files == ".jpg" \
                    or format_files == ".png" \
                    or format_files == ".svg": # перевірка файлів зображень

                photo_file.append(path_file.name)
                set_suffix_known.add(path_file.suffix)
                move_file(path_file, PATH / "photo")

            elif format_files == ".avi" \
                    or format_files == ".mp4" \
                    or format_files == ".mov" \
                    or format_files == ".mkv": # перевірка файлів відео

                video_file.append(path_file.name)
                set_suffix_known.add(path_file.suffix)
                move_file(path_file, PATH / "video")

            elif format_files == ".mp3" \
                    or format_files == ".ogg" \
                    or format_files == ".wav" \
                    or format_files == ".amr": # перевірка аудіо файлів

                audio_file.append(path_file.name)
                set_suffix_known.add(path_file.suffix)
                move_file(path_file, PATH / "audio")

            elif format_files == ".zip" \
                    or format_files == ".gz" \
                    or format_files == ".tar": # перевірка архівів

                archives_file.append(path_file.name)
                set_suffix_known.add(path_file.suffix)

            elif format_files: # перевірка інших нам невідомих файлів

                others_file.append(path_file.name)
                set_suffix_unknown.add(path_file.suffix)
                move_file(path_file, PATH / "others")

    return None


def move_file(filename: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)
    normalize_name = filename.stem
    filename.replace(target_folder / (normalize(normalize_name) + str(time.time()) + filename.suffix))


if __name__ == "__main__":
    pass


PATH = sys.argv[1]
PATH = Path(PATH)
sorter(PATH)


print(f"""Текстові файли: {text_file}")
\n\nФайли архівів: {archives_file}
\n\nАудіо файли: {audio_file}
\n\nВідео файли: {video_file}
\n\nФайли зображень: {photo_file}
\n\nНевідомі файли: {others_file}
\n\nУсі відомі розширення: {set_suffix_known}
\n\nУсі невідомі розширення: {set_suffix_unknown}
\n\nУсі папки: {folders}""")
