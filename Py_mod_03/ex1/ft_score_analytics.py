import sys


def main() -> None:
    print("=== Player Score Analytics ===")
    list_scores: list = sys.argv[1:]
    aux: int
    i: int = 1
    len_str = len(sys.argv)
    if len_str == 1:
        print("No scores provided. Usage: python3 "
              "ft_scrore_analytics.py <score1> <score2> ...")
        return
    for i in len_str:
        try:
            aux = int(list_scores[i])
        except ValueError:
            print(f"invalid parameter {i}.")
            continue
        print("No scores provided. Usage: python3 "
              "ft_scrore_analytics.py <score1> <score2> ...")

    for score in list_scores:
        print(f"Score: {score}")
    print("Total players:", len(list_scores))
    print("Average score:", sum(list_scores) / len(list_scores))
    print("High score:", max(list_scores))
    print("Low score:", min(list_scores))
    print("Score range:", max(list_scores) - min(list_scores))


if __name__ == "__main__":
    main()
