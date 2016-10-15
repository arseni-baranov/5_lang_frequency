import collections
import re


def load_data(file_name):

    with open(file_name, "r", encoding="utf-8") as text_file:
        return text_file.read().lower()


def get_most_frequent_words(text_file, top_size):
    words_in_text = re.findall(r'\w+', text_file)
    word_count = collections.Counter(words_in_text).most_common(top_size)

    return word_count

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
