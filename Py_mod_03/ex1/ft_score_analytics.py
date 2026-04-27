import sys


def main() -> None:
    print("=== Player Score Analytics ===")
    list_int_scores: list = []
    aux: int
    i: int = 1
    len_str = len(sys.argv)
    if len_str == 1:
        print("No scores provided. Usage: python3 "
              "ft_scrore_analytics.py <score1> <score2> ...")
        return
    for i in range(1, len_str):
        try:
            aux = int(sys.argv[i])
            list_int_scores.append(aux)
        except ValueError:
            print(f"Invalid parameter '{sys.argv[i]}'")
    if not list_int_scores:
        print("No scores provided. Usage: python3 "
              "ft_score_analytics.py <score1> <score2> ...")
        return

    for score in list_int_scores:
        print(f"Score: {score}")
    print("Total players:", len(list_int_scores))
    print("Average score:", sum(list_int_scores) / len(list_int_scores))
    print("High score:", max(list_int_scores))
    print("Low score:", min(list_int_scores))
    print("Score range:", max(list_int_scores) - min(list_int_scores))
    print("")


if __name__ == "__main__":
    main()
