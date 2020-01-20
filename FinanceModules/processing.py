

class Processing:

    def list_insert(self, list_data, add_value):
        list_data.insert(0, add_value)
        return list_data


    def list_adjustment(self, list_data, wont_djustment_lengeth):
        list_data_length = len(list_data)
        if list_data_length > wont_djustment_lengeth:
            del list_data[-1]
        return list_data


    def data_add_to_determinant(self, add_data, determinant_data):
        determinant_data.append(add_data)
        return determinant_data


    def processing_data(self, x, bid_price):
        return_data = [x, bid_price]
        return return_data


    def get_price_text(self, price_tag):
        for data in price_tag:
            get_price = data.text
        return get_price


    def find_html_id(self, bs_data_html, target_id):
        find_price_tag = bs_data_html.find_all("dd", id=target_id)
        return find_price_tag


    def list_data_average(self, list_data, n):
        start = n * -1 -1
        sum_value = sum(list_data[start:-1])
        average_value = sum_value / n
        return average_value, start


    def standard(self, real_price, average_price, standard_deviation):
        deviation = real_price - average_price
        standard_value = deviation / standard_deviation
        return standard_value


    def make_determinant(self, that_data, list_determinant):
        list_determinant.append(that_data)
        return list_determinant


