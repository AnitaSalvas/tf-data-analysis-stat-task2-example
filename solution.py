import pandas as pd
import numpy as np

from scipy.stats import norm

chat_id = 5072617748 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha1 = (1 - p) / 2
    alpha2 = (1 + p) / 2
    n = len(x)
    x_1 = x.max() - 0.22
    return x_1 / alpha2 ** (1 / n) + 0.22, х_1 / alpha1 ** (1 / n) + 0.22
