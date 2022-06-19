# 1 часть
# cv2.imread(*путь к файлу*,*цветовое пространство*) - загрузка изображения
# цветовые пространства: RGB — cv2.IMREAD_COLOR,
# оттенки серого — cv2.IMREAD_GRAYSCALE
# cv2.imshow(*название окна*,*переменная изображения*) - вывод изображения
# cv2.waitKey(*клавиша*) - закрытие изобржени, без этой функции открытие не будет работать
# 0 в аргументе - закрытие на любую клавишу
# cv2.imwrite(*название.расширение*, *переменная*) - сохранение изображения
# доступ к пикселям img.shape[*par*]
# par = 0, 1, 2 для цветного и 0, 1 для оттенков серого
# доступ к пикселям (b, g, r) = *переменная*[*высота*, *ширина*]
# цвета расположены в памяти в таком порядке: blue green red


# тестовая прога
import cv2

picture1 = cv2.imread("pic.jpg", cv2.IMREAD_COLOR)

# for i in range(picture1.shape[0]):
#     for j in range(picture1.shape[1]):
#         # if i == j:
#         #    picture[i, j] = [0, 0, 255]
#         if sum(picture1[i, j]) > 500:
#             picture1[i, j] = [255, 255, 255]
#         else:
#             picture1[i, j] = [0, 0, 0]
#cv2.imshow("test", picture1)
#cv2.waitKey(0)

# 2 часть
# cv2.resize(*переменная изображения*,(число, число),*метод интерполяции*) -
# изменение размера, масштабирование
# cv2.INTER_NEAREST, cv2.INTER_AREA, cv2.INTER_LINEAR (дефолт),
# cv2.INTER_CUBIC, cv2.INTER_LANCZOS4
# при кадрировании важно учитывать соотношение сторон
# cv2.warpAffine(*переменная изображения*, *матрица преобразований*, *размеры изображения*) -
# сдвиг изображения
# translation_matrix = np.float32([[1, 0, x1], [0, 1, y1]])
# *переменная изображения*[y1:y2, x1:x2] - вырез фрагмента изображения
# cv2.warpAffine(*переменная изображения*, *матрица повоорота*, (x,y)) - поворот изображения
# (x,y) - размеры изображения
# cv2.getRotationMatrix2D(*точка вращения*, *угол*, *коэфф масштабирования*)

import numpy
# picture2 = cv2.imread("pic.jpg", cv2.IMREAD_COLOR)
# size = picture2.shape[:2]
# picture2_2 = cv2.resize(picture2, (int(size[1]*.5),int(size[0]*.5)))
# transp = numpy.float32([[1,0,100],[0,1,100]])
# h, w = picture2_2.shape[:2]
# picture2_3 = cv2.warpAffine(picture2_2, transp, (w,h))
#
# crop_picture = picture2_2[100:400,100:500]
# rotation_matrix = cv2.getRotationMatrix2D((w//2,h//2), 90*2, .9)
# rotate_picture = cv2.warpAffine(picture2_2, rotation_matrix, (w,h))

# cv2.imshow("test", rotate_picture)
# cv2.waitKey(0)

# 3 часть
# OpenCV выполняет обрезку и гарантирует, что значения пикселей никогда
# не выйдут за пределы диапазона [0,255]. В numpy после достижения 255 следующим
# числом будет идти 0, а когда мы отнимаем от меньшего числа большее,
# то после 0 будет идти 255.
# cv2.split(*переменная изображения*) - разбиение на 3 или 2 канала
# сv2.merge([*каналы*]) - объединение всех каналов в один
# размытие бывает трёх видов (усреднённое, гауссово, медианное)
# усреднённое (averaging) - свёртка с ядром
# cv2.blur(*переменная изображения*, (кортеж ядра))
# гауссово (gaussian) размытие - размытие с ядром, значение которого вычислается
# как взвешенное среднее значение
# cv2.GaussianBlur(*переменная изображения*, (кортеж ядра), *стандартное отклонение*)
# по дефолту стандартное отклонение равно нулю
# медианное (median) размытие - центральный пиксель заменяется медианой всех пикселей ядра
# cv2.medianBlur(*переменная изображения*, *размер ядра*)

# операции сложения цветов:
# cv2.add cv2.substract
# приводим к типу данных uint8 (np.uint8([*число*]) - это даст верную восьмибитную арифметику
import np
# print(cv2.add(np.uint8([250]),np.uint8([50])))
# print(cv2.subtract(np.uint8([50]),np.uint8([51])))
# print(np.uint8([250])+np.uint8([50]))
# print(np.uint8([50])-np.uint8([51]))

# cv2.imshow("win", picture1)
# cv2.waitKey(0)

# инвертор цветов

h, w = picture1.shape[:2]
pic_res = cv2.resize(picture1, (int(w)//2,int(h//2)), cv2.INTER_LINEAR)
blur = cv2.blur(pic_res, (5,5))
# for i in range(picture1.shape[0]):
#     for j in range(picture1.shape[1]):
#         picture1[i][j][0] = np.uint8([255]) - np.uint8([picture1[i][j][0]])
#         picture1[i][j][1] = np.uint8([255]) - np.uint8([picture1[i][j][1]])
#         picture1[i][j][2] = np.uint8([255]) - np.uint8([picture1[i][j][2]])

cv2.imshow("win", blur)
cv2.waitKey(0)
