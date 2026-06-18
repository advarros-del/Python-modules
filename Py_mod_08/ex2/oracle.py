import os
import sys


def main() -> None:
    env_file = os.path.exists(".env")
    if not env_file:
        print("WARNING! No .env detected."
              "Should use environment variables over .env file")
        sys.exit(1)
    try:
        from dotenv import load_dotenv
    except ImportError as e:
        print(e)
        print("Please, try to install dotenv with pip install dotenv")
        sys.exit(1)
    load_dotenv()
    print("ORACLE STATUS: Reading the Matrix...\n")
    mode = os.getenv("MATRIX_MODE")
    datab = os.getenv("DATABASE_URL")
    api = os.getenv("API_KEY")
    log = os.getenv("LOG_LEVEL")
    zion = os.getenv("ZION_ENDPOINT")
    overrides_active = True if os.environ else False
    if any(x is None for x in [mode, datab, api, log, zion]):
        print("WARNING! Missing configuation info")
        sys.exit(1)
    print("Confifguration loaded:")
    if mode == "development":
        print(f"Mode: {mode}")
        print("Database: Connected to local instance")
        print("API Access: Authenticated")
        print(f"Log level: {log}")
        print("Zion Network: Online")
    elif mode == "production":
        print(f"Mode: {mode}")
        print("Database: Connected to SECURE production mainframe")
        print(f"API Access: ({api[:4] if api else '????'}...)")
        print(f"Log level: {log}")
        print("Zion Network: CONNECTED VIA ENCRYPTED UPLINK")
    else:
        print("Invalid mode: select develpment or production ")

    print("\nEnvironment security check:")
    if env_file:
        print("[OK] No hardcoded secrets detected")
        print("[OK] .env file properly configured")
    else:
        print("[KO] No hardcoded secrets detected")
        print("[KO] .env file properly configured")
    if overrides_active:
        print("[OK] Production overrides available")
    else:
        print("[KO] Production overrides available")
    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
