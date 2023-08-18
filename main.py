#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# someString = input('Введите числа через пробел: ')  # вводим числа через пробел
# someList = [int(i) for i in someString.split()]  # преобразуем строку в список
# print(min(someList))  # выводим минимальное значение списка
# indexNegNumb = []
# someListZero = []
# index = 0
# for i in someList:
#     if i < 0:
#         indexNegNumb.append(index)
#     index += 1
# print(sum(someList[(indexNegNumb[0] + 1):indexNegNumb[1]]))  # выводим сумму между двумя отрицательными числами
# print(someList)
# for i in someList:
#     if -1 <= i <= 1:
#         someListZero.append(i)
# for i in someListZero:
#     someList.remove(i)
# someList = sorted(someList)
# someListZero = sorted(someListZero)  # преобразование массива таким образом чтобы они были отсортированы опред образом
# print(someListZero + someList)

#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  someTextLorem(Текст для проверки)
# Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, deque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?


# someString = input('Введите какие нибудь предложения со знаками препинания: ')
# threeLongest = []
# for i in someString:
#     if i == '?' or i == '!':
#         someString = someString.replace(i, '.')
# someString1 = someString.split()
# someString = someString.split('. ')
# print(f'Количество предложений в тексте равно: {len(someString)}')
# print(f'Количество слов в тексте равно: {len(someString1)}')
# for i in range(3):
#     max1 = max(someString1, key=len)
#     threeLongest.append(max1)
#     max2 = max1
#     max1 = ''
#     someString1.remove(max2)
# print(f'Три самых длинных слова в тексте: {threeLongest}')

