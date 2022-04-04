from Customer import Customer


class TrackOrders:
    def __init__(self):
        self._orders_count = 0
        self._customers = dict()
        self._all_dish = set()
        self._all_days_open = set()

    # aqui deve expor a quantidade de estoque
    def __len__(self):
        return self._orders_count

    def add_new_order(self, customer, order, day):
        if customer not in self._customers:
            self._customers[customer] = Customer(customer, order, day)
        else:
            self._customers[customer].add_new_order(order, day)

        self._orders_count += 1
        self._all_dish.add(order)
        self._all_days_open.add(day)

    def get_most_ordered_dish_per_customer(self, customer):
        return self._customers[customer].most_ordered_dish_name

    def get_never_ordered_per_customer(self, customer):
        pass

    def get_days_never_visited_per_customer(self, customer):
        pass

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
