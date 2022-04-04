class TrackOrders:
    def __init__(self):
        self._orders_count = 0
        self._orders = {}

    # aqui deve expor a quantidade de estoque
    def __len__(self):
        return self._orders_count

    def add_new_order(self, customer, order, day):
        if customer not in self._orders:
            self._orders[customer] = [(order, day)]
        else:
            self._orders[customer].append((order, day))

        self._orders_count += 1

    def get_most_ordered_dish_per_customer(self, customer):
        customer_orders = {}
        most_ordered_dish_name = ""
        most_ordered_dish_count = 0

        if customer in self._orders:
            for order, _ in self._orders[customer]:
                if order not in customer_orders:
                    customer_orders[order] = 1
                else:
                    customer_orders[order] += 1

                if customer_orders[order] > most_ordered_dish_count:
                    most_ordered_dish_name = order
                    most_ordered_dish_count = customer_orders[order]

            return most_ordered_dish_name

    def get_never_ordered_per_customer(self, customer):
        pass

    def get_days_never_visited_per_customer(self, customer):
        pass

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
