import numpy as np
from decimal import Decimal

class Technical_indicator:

    def move_average_line(self, list_prices, day):
        start_day = day * -1
        array_prices = np.array(list_prices, dtype=Decimal)
        move_average_value = np.mean(array_prices[start_day:-1])
        return move_average_value


    def average_devation_rate(self, now_price, list_prices, day):
        the_aveage_range = np.array(list_prices, dtype=Decimal)
        start_day = day * -1
        average_price = np.mean(the_aveage_range[start_day: - 1])
        devation = now_price - average_price
        devation_rate = round(devation / average_price * 100, 5)
        return devation_rate


    def bollinger_band(self, list_prices, day):
        np_array = np.array(list_prices)
        start_day = day * -1
        sigma = np.std(np_array[start_day: - 1])
        return sigma


    def least_squares(self, y_list):
        # 最小二乗法
        n = 30
        x_list = [i for i in range(30)]
        x = np.array(x_list)
        y = np.array(y_list[-31:-1])
        numerator = np.dot(x, y) - y.sum() * x.sum() / n
        denominator = (x ** 2).sum() - x.sum() ** 2 / n
        slope = numerator / denominator
        intercept = (y.sum() - slope * x.sum()) / n
        return slope, intercept


    def standard_index(self, now_price, list_prices, n):
        slice_n = n * -1 - 1
        np_array = np.array(list_prices, dtype=Decimal)
        the_average = np.mean(np_array[slice_n: - 1])
        st = np.std(np_array[slice_n: -1])
        devation = now_price - the_average
        if st == 0:
            standard = 100
        else:
            sta = devation / st
            standard = sta * 10 + 100
            return standard








