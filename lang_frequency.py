import os.path, collections, re

def load_data(filepath):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_file = current_dir + '\\' + filepath
    file = open(data_file, "r", encoding="utf-8")

    return file.read().lower()


def get_most_frequent_words(textfile):
    text = re.findall(r'\w+', textfile)
    counter = collections.Counter(text)
    text = counter.most_common(10)

    return text

if __name__ == '__main__':

    filepath = ''

    while not os.path.isfile(filepath):
        try:
            words = get_most_frequent_words(load_data(input('Введите название текстового файла: ')))
            for word in words:
                print(word[0],word[1])
            exit()

        except FileNotFoundError:
            print('Данного файла не существует в директории с программой')

