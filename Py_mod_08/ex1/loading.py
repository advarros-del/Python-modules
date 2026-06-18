import sys
import importlib.metadata


def main() -> None:
    print("LOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")
    state: str
    all_ok: bool = True
    try:
        state = "[OK]"
        import pandas
        print(f"{state} pandas ({importlib.metadata.version('pandas')})"
              f" - Data manipulation ready")
    except ModuleNotFoundError:
        state = "[MISSING]"
        all_ok = False
        print(f"{state} pandas - need to install.")
    try:
        state = "[OK]"
        import numpy as np
        print(f"[{state}] numpy  ({importlib.metadata.version('numpy')}) "
              f"- Numerical computation ready")
    except ModuleNotFoundError:
        state = "[MISSING]"
        print(f"[{state}] numpy - need to install.")
        all_ok = False
        sys.exit(1)
    try:
        state = "[OK]"
        print(f"[{state}] requests ({importlib.metadata.version('requests')}) "
              f"- Network access ready")
    except ModuleNotFoundError:
        state = "[MISSING]"
        print(f"[{state}] requests - need to install.")
        all_ok = False
        sys.exit(1)
    try:
        state = "[OK]"
        import matplotlib
        print(f"[{state}] matplotlib "
              f"({importlib.metadata.version('matplotlib')}) "
              "- Visualization ready")
    except ModuleNotFoundError:
        state = "[MISSING]"
        print(f"[{state}] matplotlib - need to install.")
        all_ok = False
        sys.exit(1)

    if not all_ok:
        print("Missing dependecies detected")
        print("You need to do:")
        print("pip install -r requeriments.txt\nor")
        print("poetry install\npoetry run python loading.py")
        sys.exit(1)
    else:
        print("Analyzing Matrix data...")
        print("Processing 1000 data points...")
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
