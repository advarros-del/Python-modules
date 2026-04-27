import sys


def main() -> None:
    print("=== Inventory System Analysis ===")
    items: dict[str, int] = {}
    for arg in sys.argv[1:]:
        try:
            if arg.count(':') != 1:
                raise SyntaxError(f"Error - invalid parameter '{arg}'")
            name, quantity_str = arg.split(":")
            if name in items:
                raise KeyError(f"Redundant item '{name}' - discarding")
            quantity = int(quantity_str)
            items[name] = quantity
        except KeyError as e:
            print((e).args[0])
        except ValueError as e:
            print(f"Quantity error for {name}: {e}")
        except SyntaxError as e:
            print(f"{e}")
    print(f"Got inventory: {items}")
    aux: list = list(items.keys())
    print(f"Item list: {aux}")
    total: int = sum(items.values())
    print(f"Total quantity of the {len(items)} items: {total}")
    percent: float = 0
    for item in items:
        percent = (items[item] / total) * 100
        print(f"Item {item} represents {round(percent, 1)}%")
    most: dict[str, str | int] = {"name": "", "quantity": -1}
    for item in items:
        if items[item] > int(most["quantity"]):
            most = {"name": item, "quantity": items[item]}
    print(f"Item most abundant: "
          f"{most['name']} with quantity {most['quantity'] }")
    smallest: dict[str, str | int] = {"name": "", "quantity": 2147483647}
    for item in items:
        if items[item] < int(smallest["quantity"]):
            smallest = {"name": item, "quantity": items[item]}
    print(f"Item least abundant: {smallest['name']}"
          f"with quantity {smallest['quantity']}")
    items.update({"magic_item": 1})
    print(f"Updated inventory: {items}")


if __name__ == "__main__":
    main()
