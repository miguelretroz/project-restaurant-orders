class DishCount(dict):
    def __init__(self, dish):
        self[dish] = 1

    def __missing__(self, key):
        return 0


class Customer():
    def __init__(self, name, first_order, first_day):
        self.name = name
        self.orders = [(first_order, first_day)]
        self.dishes = {first_order}
        self.days = {first_day}
        self.most_ordered_dish_name = first_order
        self.most_ordered_dish_counts = DishCount(first_order)

    def check_most_ordered_dish(self, dish):
        actual_most_ordered_value = self.most_ordered_dish_counts[
            self.most_ordered_dish_name]

        if self.most_ordered_dish_counts[dish] > actual_most_ordered_value:
            self.most_ordered_dish_name = dish

    def add_new_order(self, order, day):
        self.orders.append((order, day))
        self.dishes.add(order)
        self.days.add(day)

        self.most_ordered_dish_counts[order] += 1
        self.check_most_ordered_dish(order)
