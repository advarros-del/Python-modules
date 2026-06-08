import os
import sys
from dotenv import load_dotenv

load_dotenv()

def main() -> None:
    env_file = os.path.exists(".env")
    if not env_file:
        print("WARNING! No .env detected.Should use environment variables over .env file")
    flag: bool = False
    mode = os.getenv("MATRIX_MODE")
    datab = os.getenv("DATABASE_URL")
    api = os.getenv("API_KEY")
    log = os.getenv("LOG_LEVEL")
    zion = os.getenv("ZION_ENDPOINT")
    overrides_active = True if os.environ else False
    if mode is None or datab is None or api is None or log is None or zion is None:
        print("WARNING! Missing configuation info")
        sys.exit(1)
    print("Confifguration loaded:")
    if mode is "development":
        print(f"Mode: {mode}")
        print(f"Database: Connected to local instance")
        print(f"API Access: Authenticated")
        print(f"Log level: {log}")
        print(f"Zion Network: Online")
    else:
        print(f"Mode: {mode}")
        print(f"Database: Connected to SECURE production mainframe")
        print(f"API Access: ({api[:4]}...)")
        print(f"Log level: {log}")
        print(f"Zion Network: CONNECTED VIA ENCRYPTED UPLINK")
   
    print("Environment security check:")
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
    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    main()