import abc
import typing
from typing import Any


class DataProcessor(abc.ABC):
    def __init__(self, data: typing.Any, counter: int, queue: list) -> None:
        self.counter = counter
        self.queue = queue

    @abc.abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abc.abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        aux: tuple[int, str] = self.queue.pop(0)
        return aux


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list) and all(
            isinstance(item, (int, float)) for item in data
        ):
            return True
        else:
            return False

    def ingest(self, data) -> None:
        if self.validate(data) is True:
            if isinstance(data, list):
                for item in data:
                    self.queue.append((self.counter, [str(item)]))
                    self.counter += 1
            else:
                self.queue.append((self.counter, str(data)))
                self.counter += 1
        else:
            raise ValueError("Got exception: Improper numeric data")


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list) and all(
            isinstance(item, str) for item in data
        ):
            return True
        else:
            return False

    def ingest(self, data) -> None:
        if self.validate(data) is True:
            if isinstance(data, list):
                for item in data:
                    self.queue.append((self.counter, str(item)))
                    self.counter += 1
            else:
                self.queue.append((self.counter, str(data)))
                self.counter += 1
        else:
            raise ValueError("Got exception: Improper text data")


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, dict) and len(data) == 2:
            return True
        if isinstance(data, list) and all(
            isinstance(item, dict) and len(item) == 2 for item in data
        ):
            return True
        else:
            return False

    def ingest(self, data) -> None:
        clear_text: str
        if self.validate(data) is True:
            if isinstance(data, list):
                for item in data:
                    clear_text = ", ".join(
                        [f"{key}: {value}" for key, value in item.items()])
                    self.queue.append((self.counter, clear_text))
                    self.counter += 1
            else:
                clear_text = ", ".join(
                    [f"{key}: {value}" for key, value in data.items()])
                self.queue.append((self.counter, clear_text))
                self.counter += 1
        else:
            raise ValueError("Got exception: Improper log data")


def main() -> None:
    print("=== Code Nexus - Data Processor ===\n")
    numeric_queue = NumericProcessor(0, 0, [])
    text_queue = TextProcessor("", 0, [])
    log_queue = LogProcessor({}, 0, [])
    number: int = 42
    number2: str = "Hello"
    text: int = 42
    log: str = "Hello"
    foo_thing: str = "foo"
    numeric_list: list = [1, 2, 3, 4, 5]
    text_list: list = ["Hello", "Nexus", "World"]
    Log_list: list = [
        {'log_level': 'NOTICE', 'log_message': 'Connection to server'},
        {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}]
    i: int = 0
    print("Testing Numeric Processor...")
    print(f" Trying to validate input '{number}': "
          f"{numeric_queue.validate(number)} ")
    print(f" Trying to validate input '{number2}': "
          f"{numeric_queue.validate(number2)} ")
    try:
        print(f" Testing invalid ingestion on string "
              f"'{foo_thing}' without validation:")
        numeric_queue.ingest(foo_thing)
    except ValueError as e:
        print(f" {e}")
    print(f" Procesing data: {numeric_list}")
    numeric_queue.validate(numeric_list)
    numeric_queue.ingest(numeric_list)
    print(" Extracting 3 values ...")
    h: tuple
    while i < 3:
        h = numeric_queue.output()
        print(f" Numeric value {h[0]}: {h[1]}")
        i += 1
    print("\nTesting Text Processor...")
    print(f" Trying to validate input {text}: {text_queue.validate(text)} ")
    print(f" Processing data: {text_list}")
    text_queue.validate(text_list)
    text_queue.ingest(text_list)
    print(" Extracting 1 value...")
    i = 0
    while i < 1:
        index, data = text_queue.output()
        print(f" Text value {index}: {data}")
        i += 1
    print("\nTesting Log Processor...")
    print(f" Trying to validate input {log}: {log_queue.validate(log)} ")
    print(f" Processing data: {Log_list}")
    log_queue.validate(Log_list)
    log_queue.ingest(Log_list)
    print(" Extracting 2 values...")
    i = 0
    while i < 2:
        h = log_queue.output()
        print(f" Log value {h[0]}: {h[1]}")
        i += 1


if __name__ == "__main__":
    main()
