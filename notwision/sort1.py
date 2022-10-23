from pathlib import Path
from normalize import normalize
import sys


#Списки файлів


text_file = []
audio_file = []
video_file = []
photo_file = []
archives_file = []
others_file = []
set_suffix_known = set()
set_suffix_unknown = set()


def sorter(path=sys.argv[1]): # функція сортування файлів
    path = Path(path)

    for i in path.iterdir(): # ітерація по файлах та папках за вказаним шляхом
        new_path_name = normalize(path.stem) # нове ім’я
        new_path_name = new_path_name + path.suffix
        new_path_name = Path(new_path_name)
        new_path = path.joinpath(i)
        new_path.rename(new_path_name)

        if i.is_dir(): # якщо папка то заходимо в неї рекурсивно викликаємо функцію
            sorter(path / i)

        if i.is_file(): # якщо файл перевіряємо розширення та додаємо інформацію до списків
            path = path / i
            format_files = path.suffix

            if format_files == ".txt" \
                    or format_files == ".doc" \
                    or format_files == ".docx" \
                    or format_files == ".pdf" \
                    or format_files == ".pptx" \
                    or format_files == ".xlsx": # перевірка текстових файлів

                text_file.append(path.name)
                set_suffix_known.add(path.suffix)

            elif format_files == ".jpeg" \
                    or format_files == ".jpg" \
                    or format_files == ".png" \
                    or format_files == ".svg": # перевірка файлів зображень

                photo_file.append(path.name)
                set_suffix_known.add(path.suffix)

            elif format_files == ".avi" \
                    or format_files == ".mp4" \
                    or format_files == ".mov" \
                    or format_files == ".mkv": # перевірка файлів відео

                video_file.append(path.name)
                set_suffix_known.add(path.suffix)

            elif format_files == ".mp3" \
                    or format_files == ".ogg" \
                    or format_files == ".wav" \
                    or format_files == ".amr": # перевірка аудіо файлів

                audio_file.append(path.name)
                set_suffix_known.add(path.suffix)

            elif format_files == ".zip" \
                    or format_files == ".gz" \
                    or format_files == ".tar": # перевірка архівів

                archives_file.append(path.name)
                set_suffix_known.add(path.suffix)

            elif format_files: # перевірка інших нам невідомих файлів

                others_file.append(path.name)
                set_suffix_unknown.add(path.suffix)

    return None


# def move_file()

if __name__ == "__main__":
    pass


sorter()

print(f"Текстові файли: {text_file}")
print(f"Файли архівів: {archives_file}")
print(f"Аудіо файли: {audio_file}")
print(f"Відео файли: {video_file}")
print(f"Файли зображень: {photo_file}")
print(f"Невідомі файли: {others_file}")
print(f"Усі відомі розширення: {set_suffix_known}")
print(f"Усі невідомі розширення: {set_suffix_unknown}")