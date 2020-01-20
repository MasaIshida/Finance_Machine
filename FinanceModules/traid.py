

class Simulated_traid:

    def buy(self, money, price):
        buy_price = money / price + 0.003
        potision = "call"
        return round(buy_price, 0), potision

    def sell(self, have_doll, price):
        sell_price = have_doll * price - 0.003
        potision = "put"
        return sell_price, potision

    def profit(self, before_price, after_price, divi_list):
        divi = after_price - before_price
        divi_list.append(divi)
        return divi_list


