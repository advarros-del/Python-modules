import abc
import typing
from typing import Any

class DataProcessor(abc.ABC):
    def __init__(self, data: Any, counter: int, queue: list) -> None:
        self.counter = counter
        self.queue = queue

    @abc.abstractmethod
    def validate(self, data:Any) -> bool:
        pass

    @abc.abstractmethod
    def ingest(self, data:Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        return (self.code, str(self.data)) 


class NumericProcessor(DataProcessor):    
    def validate(self, data: Any) -> bool:
        if isinstance (data, (int, float)):
            return True
        if isinstance(data, list) and all(isinstance(item, (int, float)) for item in data):
            return True
        else:
            return False
    def ingest(self, data) -> None:
        if self.validate(data) == True:
            if isinstance(data, list):
                for item in data:
                    self.queue.append((self.counter, [str(item)]))
                    self.counter += 1
            else:
                self.queue.append((self.counter, str(data)))
                self.counter += 1
        else:
            raise ValueError("Got exception: Improper numeric data")
    def output(self) -> tuple[int, str]:
        aux: tuple[int, str] = self.queue.pop(0)
        return aux


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list) and all(isinstance(item, str) for item in data):
            return True
        else:
            return False
    def ingest(self, data) -> None:
        if self.validate(data) == True:
            if isinstance(data, list):
                for item in data:
                    self.queue.append((self.counter, [str(item)]))
                    self.counter += 1
            else:
                self.queue.append((self.counter, str(data)))
                self.counter += 1
        else:
            raise ValueError("Got exception: Improper text data")
    def output(self) -> tuple[int, str]:
        aux: tuple[int, str] = self.queue.pop(0)
        return aux


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, dict) and len(data) == 2:
            return True
        if isinstance(data, list) and all(isinstance(item, dict) and len(item) == 2 for item in data):
            return True
        else:
            return False
    def ingest(self, data) -> None:
        if self.validate(data) == True:
            if isinstance(data, list):
                for item in data:
                    texto_limpio: str = ", ".join([f"{key}: {value}" for key, value in item.items()])
                    self.queue.append((self.counter, texto_limpio))
                    self.counter += 1
            else:
                texto_limpio: str = ", ".join([f"{key}: {value}" for key, value in data.items()])
                self.queue.append((self.counter, texto_limpio))
                self.counter += 1
        else:
            raise ValueError("Got exception: Improper log data")
    def output(self) -> tuple[int, str]:
        aux: tuple[int, str] = self.queue.pop(0)
        return aux

class DataStream:
    def __init__(self) -> None:
        self.processors: list[DataProcessor] = []
        self.class_list = [NumericProcessor, TextProcessor, LogProcessor]   
    
    def register_processor(self, proc: DataProcessor) -> None:
        self.processors.append(proc)

    def process_stream(self, stream: list[typing.Any]) -> None:
        for item in stream:
            for processor in self.processors:
                try:
                    if processor.validate(item):
                        processor.ingest(item)
                        break
                except ValueError as e:
                    print(f"Datastream error - Can't process in stream: {item}")

    def print_processors_stats(self) -> None:
        if not self.processors:
            print("No processors found, not data")
            return
        print("=== DataStream statistics ===")
        for processor in self.processors:
            print(f"{processor.__class__.__name__}: total {processor.counter} items processed, remaining {len(processor.queue)} on processor)")

def main() -> None:
    print("=== Code Nexux - Data Stream ===\n")
    print("Initializing data stream...")
    data_stream = DataStream()
    data_stream.print_processors_stats()
    print("\nRegistering Numeric Processor\n")
    numeric_processor = NumericProcessor(0, 0, [])
    text_processor = TextProcessor(0, 0, [])
    log_processor = LogProcessor(0, 0, [])
    data_stream.register_processor(numeric_processor)
    data_stream.register_processor(text_processor)
    data_stream.register_processor(log_processor)
    random_data = ["Hello world", [3.14, -1, 2.71], [{"log_level": "WARNING", "log_message": "Telnet access! Use ssh instead"}, {"log_level": "INFO", "log_message": "User will is connected"}], 42, ["Hi", "five"]]
    print(f"Send first batch of data on stream: {random_data}")
    data_stream.process_stream(random_data)
    data_stream.print_processors_stats()
    for _ in range(3):
        data_stream.processors[0].output()
    for _ in range(2):
        data_stream.processors[1].output()
    for _ in range(1):
        data_stream.processors[2].output()
    data_stream.print_processors_stats()
        
    
if __name__ == "__main__":
    main()