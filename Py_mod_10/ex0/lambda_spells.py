def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return list(sorted(artifacts, key=lambda x: -x["power"]))


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda x: x["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda x: "*" + x + "*", spells))


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
        {'name': 'Crystal Orb', 'power': 85, 'type': 'radiant'},
        {'name': 'fire Staff', 'power': 92, 'type': 'fire'},
        {'name': 'Staff of Python', 'power': 90, 'type': 'invocation'}
        ]
    mages: list[dict[str, str | int]] = [
        {'name' : 'Juan Tamariz', 'power': 1200, "element": "Card"},
        {'name' : 'Yunke', 'power': 600, "element": "Chains"},
        {'name' : 'Tomas Ridle', 'power': 1800, "element": "Darkness"}
    ]
    spells: list[str] = ["fireball", "heal", "shield"]
    print("\nTesting artifact sorter...")
    is_sorted: list = artifact_sorter(artifacts)
    print(f"{artifacts[0]['name']} ({artifacts[0]['power']} power) comes before " 
        f" {artifacts[1]['name']} ({artifacts[1]['power']} power)")
    the_mages: list[dict] = power_filter(mages, 1000)
    for mage in the_mages:
        print(f"{mage[0]['name']} with {mage[0]['power']} power, have the element {mage[0]['element']}.")
    spelling: list[str] = spell_transformer(spells)
    print(spelling)
    stats: dict = mage_stats(mages)
    for key, value in stats:
        print(f"{key}: {value}")