import random


def main() -> None:
    print("=== Game Data Alchemist ===\n")
    initial_list = ("Alice", "bob", "Charlie", "dylan", "Emma", "Gregory", "john", "kevin", "Liam")
    final_cap_list: list[str] = [name.capitalize() for name in initial_list]
    original_cap_list: list[str] = [name for name in initial_list if name.capitalize() == name]
    print(f"Initial list of players: {initial_list}")
    print(f"New list with capitalized names: {final_cap_list}")
    print(f"New list of capitalized names only: {original_cap_list}\n")
    score_this: dict[str, int] = {name: random.randint(0, 1000) for name in final_cap_list}
    print(f"Score dict: {score_this}")
    print(f"Score average: {sum(score_this.values()) / len(score_this):.2f}")
    highest_score: dict[str, int] = {name: score_this[name] for name in score_this if score_this[name] > sum(score_this.values()) / len(score_this)}
    print(f"High score: {highest_score}")

if __name__ == "__main__":
    main()
        