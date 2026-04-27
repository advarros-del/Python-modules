import typing
import random


def gen_event() -> typing.Generator[tuple, None, None]:
    players: list[str] = ["Alice", "Bob", "Charlie", "Dylan"]
    actions: list[str] = ["run", "eat", "grab", "swim", "sleep", "move"]

    while True:
        player: str = random.choice(players)
        action: str = random.choice(actions)
        yield (player, action)


def consume_events(event_list: list[tuple]) -> typing.Generator[
        tuple, None, None]:
    while len(event_list) > 0:
        i = random.randrange(len(event_list))
        one_less: tuple = event_list[i]
        event_list.pop(i)
        yield one_less


def main() -> None:
    print("=== Data Stream Analysis ===")
    events_gen = gen_event()
    for n in range(1000):
        event = next(events_gen)
        print(f"Event {n}: Player {event[0]} did action {event[1]}")
    list_events: list[tuple] = [next(events_gen) for _ in range(10)]
    print(f"Built list of 10 events: {list_events}")
    one_less_gen = consume_events(list_events)
    for _ in range(0, len(list_events)):
        event = next(one_less_gen)
        print(f"Got event from the list: {event}")
        print(f"Remain in list: {list_events}")


if __name__ == "__main__":
    main()
