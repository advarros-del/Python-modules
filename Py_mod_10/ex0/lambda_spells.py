def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return list(sorted(artifacts, key=lambda x: -x["power"]))


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda x: x["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda x: "* " + x + " *", spells))


def mage_stats(mages: list[dict]) -> dict:
    maximun = max(mages, key=lambda x: x["power"])
    minimun = min(mages, key=lambda x: x["power"])
    average = round(sum(map(lambda x: x["power"], mages)) / len(mages), 2)
    return {
        "max_power": maximun["power"],
        "min_power": minimun["power"],
        "avg_power": average
    }


def main() -> None:
    artifacts: list[dict[str, str | int]] = [
        {'name': 'Crystal Orb', 'power': 92, 'type': 'radiant'},
        {'name': 'fire Staff', 'power': 85, 'type': 'fire'},
        {'name': 'Staff of Python', 'power': 90, 'type': 'invocation'},
        {'name': 'Zenith', 'power': 190, 'type': 'Sword'}
        ]
    mages: list[dict[str, str | int]] = [
        {'name': 'Juan Tamariz', 'power': 1200, "element": "Card"},
        {'name': 'Yunke', 'power': 600, "element": "Chains"},
        {'name': 'Tomas Ridle', 'power': 1800, "element": "Darkness"}
    ]
    spells: list[str] = ["fireball", "heal", "shield"]
    print("\nTesting artifact sorter...")
    sorted_arts = artifact_sorter(artifacts)
    res_arts = ""
    for art in sorted_arts:
        if art != sorted_arts[0]:
            res_arts += " comes before "
        res_arts += f"{art['name']} ({art['power']} power)"
    print(res_arts)
    the_mages: list[dict] = power_filter(mages, 1000)
    for mage in the_mages:
        print(f"{mage['name']} with {mage['power']} power, "
              f"have the element {mage['element']}.")
    print("\nTesting spell transformer...")
    print(*spell_transformer(spells))
    stats: dict = mage_stats(mages)
    print("\nTesting mage stats...")
    for key, value in stats.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
