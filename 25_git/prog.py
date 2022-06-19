from re import fullmatch

def transformation(inp_):
    mask_ = inp_.replace("?", "\d")
    mask_ = mask_.replace("*", "\d*")
    return mask_

# проверка соответствия, возвращает true или false
def conformity(mask_, i):
    return fullmatch(mask_, i)

# ввод из условия
mask = transformation() # сюда вводить маску в виде строки, функция
                        # переделает её в нужный вид

