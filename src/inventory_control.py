from track_orders import TrackOrders


class InventoryControl:
    INGREDIENTS = {
        'hamburguer': {'pao', 'carne', 'queijo'},
        'pizza': {'massa', 'queijo', 'molho'},
        'misto-quente': {'pao', 'queijo', 'presunto'},
        'coxinha': {'massa', 'frango'},
    }
    MINIMUM_INVENTORY = {
        'pao': 50,
        'carne': 50,
        'queijo': 100,
        'molho': 50,
        'presunto': 50,
        'massa': 50,
        'frango': 50,
    }

    def __init__(self):
        self._orders = TrackOrders()
        self._quantities_to_buy = {
            'pao': 0,
            'carne': 0,
            'queijo': 0,
            'molho': 0,
            'presunto': 0,
            'massa': 0,
            'frango': 0,
        }
        self.dishes = {'hamburguer', 'pizza', 'misto-quente', 'coxinha'}
        self.ingredients_not_available = set()

    def add_new_order(self, customer, order, day):
        self._orders.add_new_order(customer, order, day)

        has_ingredient_not_available = self.INGREDIENTS[order].intersection(
            self.ingredients_not_available)
        if len(has_ingredient_not_available) > 0:
            return False

        for ingredient in self.INGREDIENTS[order]:
            self._quantities_to_buy[ingredient] += 1

            remaining_ingredient = self.MINIMUM_INVENTORY[ingredient] - (
                self._quantities_to_buy[ingredient]
                )
            if not remaining_ingredient:
                self.ingredients_not_available.add(ingredient)
                self.dishes.discard(order)

    def get_quantities_to_buy(self):
        return self._quantities_to_buy

