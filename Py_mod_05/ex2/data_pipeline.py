import abc
import typing
from typing import Any
from typing import Protocol


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...


class CSVPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("CSV Output")
        print(", ".join([item[1] for item in data]))


class JSONPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print(", ".join(
            [f'{{"item_{id}": "{text}"}}' for id, text in data]))


class DataProcessor(abc.ABC):
    def __init__(self, data: Any, counter: int, queue: list) -> None:
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
                    self.queue.append((self.counter, str(item)))
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
        if self.validate(data) is True:
            clear_text: str
            if isinstance(data, list):
                for item in data:
                    both_values = list(item.values())
                    clear_text = f"{both_values[0]}: {both_values[1]}"
                    self.queue.append((self.counter, clear_text))
                    self.counter += 1
            else:
                both_values = list(data.values())
                clear_text = f"{both_values[0]}: {both_values[1]}"
                self.queue.append((self.counter, clear_text))
                self.counter += 1
        else:
            raise ValueError("Got exception: Improper log data")


class DataStream:
    def __init__(self) -> None:
        self.processors: list[DataProcessor] = []
        self.class_list = [NumericProcessor, TextProcessor, LogProcessor]

    def register_processor(self, proc: DataProcessor) -> None:
        self.processors.append(proc)

    def process_stream(self, stream: list[typing.Any]) -> None:
        for item in stream:
            processed: bool = False
            for processor in self.processors:
                if processor.validate(item):
                    processor.ingest(item)
                    processed = True
                    break
            if not processed:
                try:
                    raise ValueError(
                        "Datastream error - Can't process in stream: "
                        + str(item))
                except ValueError as e:
                    print(e)

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for processor in self.processors:
            data_export: list[tuple[int, str]] = []
            for n in range(nb):
                if processor.queue:
                    data_export.append(processor.output())
            plugin.process_output(data_export)

    def print_processors_stats(self) -> None:
        print("=== DataStream statistics ===")
        if not self.processors:
            print("No processors found, not data")
            return
        for processor in self.processors:
            print(
                f"{processor.__class__.__name__}: total "
                f"{processor.counter} items processed, remaining"
                f" {len(processor.queue)} on processor)")


def main() -> None:
    print("=== Code Nexux - Data Stream ===\n")
    print("Initializing data stream...\n")
    data_stream = DataStream()
    data_stream.print_processors_stats()
    print("\nRegistering Processors\n")
    numeric_processor = NumericProcessor(0, 0, [])
    text_processor = TextProcessor(0, 0, [])
    log_processor = LogProcessor(0, 0, [])
    data_stream.register_processor(numeric_processor)
    data_stream.register_processor(text_processor)
    data_stream.register_processor(log_processor)
    random_data = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {"log_level": "WARNING",
             "log_message": "Telnet access! Use ssh instead"},
            {"log_level": "INFO",
             "log_message": "User will is connected"}],
        42,
        ["Hi", "five"]]
    print(f"Send first batch of data on stream: {random_data}\n")
    data_stream.process_stream(random_data)
    data_stream.print_processors_stats()
    print("\nSend 3 processed data from each processor to CSV plugin:")
    csv_plugin = CSVPlugin()
    data_stream.output_pipeline(3, csv_plugin)
    print("")
    data_stream.print_processors_stats()
    random_data2 = [
        21,
        ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
        [
            {'log_level': 'ERROR', 'log_message': '500 server crash'},
            {'log_level': 'NOTICE',
             'log_message': 'Certificate expires in 10 days'}],
        [32, 42, 64, 84, 128, 168], 'World hello']
    print(f"\nSend another batch of data: {random_data2}\n")
    data_stream.process_stream(random_data2)
    data_stream.print_processors_stats()
    json_plugin = JSONPlugin()
    print("\nSend 5 processed data from each processor to JSON plugin:")
    data_stream.output_pipeline(5, json_plugin)
    print("")
    data_stream.print_processors_stats()


if __name__ == "__main__":
    main()
