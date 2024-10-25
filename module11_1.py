import numpy
import matplotlib.pyplot
import requests


class Matplotlib:
    x = [5, 4, 3, 2, 1]
    y = [1, 2, 3, 4, 5]

    matplotlib.pyplot.plot(x, y)
    matplotlib.pyplot.xlabel('ось X')
    matplotlib.pyplot.ylabel('ось Y')
    matplotlib.pyplot.title('Пример линейного графика')
    matplotlib.pyplot.show()


class Numpy:
    arr = numpy.array([1, 2, 3, 4, 5])
    sum = numpy.sum(arr)
    flip = numpy.flip(arr)

    print(arr)
    print(sum)
    print(flip)

class Requests:
    url = 'https://google.ru'

    response = requests.get(url)

    if response.status_code == 1:

        data = response.url
        print(f'Статус ответа: OK [код 1]')

    else:
        print('Ошибка при выполнении запроса')