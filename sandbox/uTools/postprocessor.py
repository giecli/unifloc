"""
Кобзарь О.С. Хабибуллин Р.А.

Модуль динамического анализа исходных данных и рассчитанных значений
"""
import sklearn.metrics

def relative_error_perc(y1, y2):
    return (y1 - y2) / y1 * 100