import os.path
import collections
import re


def load_data(file_name):

    current_dir = os.path.abspath(__file__)
    script_name = os.path.basename(__file__)

    data_file = current_dir.replace(script_name, '') + file_name

    with open(data_file, "r", encoding="utf-8") as data_file:
        return data_file.read().lower()


def get_most_frequent_words(text_file, top_size):
    text = re.findall(r'\w+', text_file)
    counter = collections.Counter(text)
    text = counter.most_common(top_size)

    return text

if __name__ == '__main__':

    file_path = None

    while file_path is None:
        try:
            words = get_most_frequent_words(load_data(input('Введите название текстового файла: ')), 10)
            for word, word_frequency in words:
                print(word, word_frequency)
            exit()

        except FileNotFoundError:
            print('Данного файла не существует в директории с программой')

