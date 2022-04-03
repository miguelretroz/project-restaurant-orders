import csv


def analdo_dish_count(client, dish, dish_to_count, clients):
    if client == "arnaldo" and dish == dish_to_count:
        clients[client][f"{dish_to_count}_count"] += 1


def clients_operations(client, dish, day, clients):
    if client == "maria":
        if dish not in clients["maria"]["odr_cnt"]:
            clients["maria"]["odr_cnt"][dish] = 1
        else:
            clients["maria"]["odr_cnt"][dish] += 1

        if clients["maria"]["odr_cnt"][dish] > clients["maria"]["most_rq_cnt"]:
            clients["maria"]["most_rq_name"] = dish
            clients["maria"]["most_rq_cnt"] = clients["maria"]["odr_cnt"][dish]

    elif client == "joao":
        clients["joao"]["dishes_requested"].add(dish)
        clients["joao"]["day_in_restaurant"].add(day)

    analdo_dish_count(client, dish, "hamburguer", clients)


def analyze_log(path_to_file):
    if not path_to_file.endswith(".csv"):
        raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")

    try:
        with open(path_to_file) as file:
            orders = csv.reader(file, delimiter=",", quotechar="\"")
            _, *data = orders

            clients = {
                "maria": {
                    "odr_cnt": {},
                    "most_rq_name": "",
                    "most_rq_cnt": 0
                },
                "arnaldo": {
                    "hamburguer_count": 0
                },
                "joao": {
                    "dishes_requested": set(),
                    "day_in_restaurant": set(),
                }
            }

            days_of_operation = set()
            all_dishes = set()

            for client, dish, day in data:
                days_of_operation.add(day)
                all_dishes.add(dish)
                clients_operations(client, dish, day, clients)

            maria_most_requested = clients["maria"]["most_rq_name"]
            joao_never_requested = all_dishes.difference(
                clients["joao"]["dishes_requested"])
            joao_never_in_restaurant = days_of_operation.difference(
                clients["joao"]["day_in_restaurant"])

            arnaldo_hamburguer_count = clients["arnaldo"]["hamburguer_count"]

            with open("data/mkt_campaign.txt", "w") as file:
                file.writelines([
                    f"{maria_most_requested}\n",
                    f"{arnaldo_hamburguer_count}\n",
                    f"{joao_never_requested}\n",
                    f"{joao_never_in_restaurant}\n",
                ])
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")
