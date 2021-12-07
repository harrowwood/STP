import argparse
import os
import random

ap = argparse.ArgumentParser()

ap.add_argument("-p", '--path', required=True, help="Inter path to text data", default='data/')
ap.add_argument("-v", "--verse", required=True, help='Inter numbers of verse')
ap.add_argument("-c", "--chorus", required=True, help='inter numbers of chorus')
ap.add_argument("-o", "--out_path", help="Inter out path to save data", default='output/')

args = vars(ap.parse_args())


class Crawler:

    def __init__(self, path):
        self.path = path

    @staticmethod
    def open_file(_path):
        with open(_path) as f:
            return f.read()

    def read_text(self):
        data = {'Куплет': [],
                'Припев': []}
        for l, i in enumerate(os.listdir(self.path)):
            [data['Куплет'].append(item) if 'Куплет' in item else data['Припев'].append(item) for item in
             self.open_file(self.path + i).split('\n\n')]
        return data


class Gena:

    def __init__(self, text_data, num_verse, num_chorus):
        self.text_data = text_data,
        self._num_verse = num_verse,
        self._num_chorus = num_chorus

    def gen(self):
        data = {'Куплет': [],
                'Припев': []}
        for _ in ['Куплет', 'Припев']:
            for i in self.text_data[0][_]:
                for item in i.split('\n'):
                    if _ not in item:
                        data[_].append(item)
            random.shuffle(data[_])
        data['Припев'] = data['Припев'][:self._num_chorus]
        data['Куплет'] = data['Куплет'][:self._num_verse[0]]
        return data


class Saver:

    def __init__(self, data, path):
        self.data = data
        self.path = path

    @staticmethod
    def _split_data():
        return lambda X, n = 3: [X[i::n] for i in range(0,  n)]

    def save_file(self):
        with open(self.path + '1.txt', 'w') as f:
            for i, item in enumerate(self._split_data()(self.data['Куплет'])):
                f.write(f'Куплет {i+1} \n\n')
                f.write('\n'.join(item) + '\n\n')
                f.write(f'Припев {i + 1} \n\n')
                f.write('\n'.join(self.data['Припев']) + '\n\n')


def bubble_sort_dict(data):
    """
    Нужно сделать пузырьковый алгоритм сортировки на hash table(я использовал dict)
    обычный алгоритм выглядит так:
        def bubble_sort(nums):
            flag = True
            while flag:
            flag = False
            for i in range(len(nums) - 1):
                if nums[i] > nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
                    flag = True
            return nums

    Структура:
    Тут так же все просто:
    1. Нужен флаг на завершение сортировки, если флага не будет, алгоритм зайдет в цикл
    2. Проверяем 2 элемента массива, текущий и текущий + 1
    3. Если текущий больше, то меняем их местами и так продолжаем, пока этих изменений не будет
    Сложность данного алгоритма: O(n2)

    :param data: dict
    :return: sorted dict
    """
    print(data)
    my_list = list(data.items())
    for mx in range(len(my_list)-1, -1, -1):
        swapped = False
        for i in range(mx):
            if my_list[i][1] < my_list[i+1][1]:
                my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
                swapped = True
        if not swapped:
            break
    print(my_list)
    return my_list


if __name__ == "__main__":
    text = Crawler(args['path']).read_text()
    new_data = Gena(text, int(args['verse']), int(args['chorus'])).gen()
    Saver(new_data, args['out_path']).save_file()

    bubble_sort_dict({"m": 1, "i": 4, "s": 4, "P": 2})