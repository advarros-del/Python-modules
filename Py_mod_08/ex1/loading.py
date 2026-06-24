import sys
import importlib.metadata


def main() -> None:
    print("LOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")
    all_ok: bool = True
    dependences_list: list = ["pandas", "numpy", "requests", "matplotlib"]
    for dependence in dependences_list:
        try:
            version = importlib.metadata.version(dependence)
            print(f"[OK] {dependence} ({version})"
                  f" - Data manipulation ready")
        except Exception:
            print(f"[MISSING] {dependence}")
            all_ok = False
    if not all_ok:
        print("Missing dependecies detected")
        print("You need to do:")
        print("pip install -r requeriments.txt\nor")
        print("poetry install\npoetry run python loading.py")
        sys.exit(1)
    else:
        print("Analyzing Matrix data...")
        print("Processing 1000 data points...")
        import numpy as np
        import pandas
        import matplotlib
        numbers: np.ndarray = np.random.randint(0, 1000, size=1000)
        data_tablet = pandas.DataFrame(numbers)
        import matplotlib.pyplot
        matplotlib.pyplot.hist(data_tablet)
        print("Generating visualization...")
        matplotlib.pyplot.savefig("matrix_graphics.png")
        matplotlib.pyplot.close()
        print("\nAnalysis complete!")
        print("Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    main()
