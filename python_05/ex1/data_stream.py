#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):

    def __init__(self) -> None:
        self._data: list[str] = []
        self._total_processed: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        ...

    @abstractmethod
    def ingest(self, data: Any) -> None:
        ...

    def output(self) -> tuple[int, str]:
        if not self._data:
            raise IndexError("No data available in processor")
        return (self.total_processed - self.remaining, self._data.pop(0))

    @property
    def total_processed(self) -> int:
        return self._total_processed

    @property
    def remaining(self) -> int:
        return len(self._data)


class NumericProcessor(DataProcessor):
    @staticmethod
    def _is_numeric(val: Any) -> bool:
        return isinstance(val, (int, float)) and not isinstance(val, bool)

    def validate(self, data: Any) -> bool:
        return (
            self._is_numeric(data)
            or (
                isinstance(data, list)
                and len(data) > 0
                and all(self._is_numeric(item) for item in data)
            )
        )

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")
        if isinstance(data, list):
            for item in data:
                self._data.append(str(item))
                self._total_processed += 1
        else:
            self._data.append(str(data))
            self._total_processed += 1


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        return (
            isinstance(data, str)
            or (
                isinstance(data, list)
                and len(data) > 0
                and all(isinstance(item, str) for item in data)
            )
        )

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")
        if isinstance(data, list):
            for item in data:
                self._data.append(item)
                self._total_processed += 1
        else:
            self._data.append(data)
            self._total_processed += 1


class LogProcessor(DataProcessor):
    @staticmethod
    def _is_valid_dict(data: dict[str, str]) -> bool:
        return all(
            isinstance(k, str) and isinstance(v, str)
            for k, v in data.items()
        )

    def validate(self, data: Any) -> bool:
        return (
            (
                isinstance(data, dict)
                and self._is_valid_dict(data)
            )
            or (
                isinstance(data, list)
                and len(data) > 0
                and all(
                    isinstance(item, dict)
                    and self._is_valid_dict(item)
                    for item in data
                )
            )
        )

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")
        items: list[dict[str, str]] = (
            data if isinstance(data, list) else [data]
        )
        for entry in items:
            formatted = ": ".join(entry.values())
            self._data.append(formatted)
            self._total_processed += 1


class DataStream:
    def __init__(self) -> None:
        self._processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for element in stream:
            for proc in self._processors:
                if proc.validate(element):
                    proc.ingest(element)
                    break
            else:
                print(
                    "DataStream error - Can't process "
                    f"element in stream: {element}"
                )

    @staticmethod
    def _camel_case_closed(name: str) -> str:
        return "".join(f" {char}" if char.isupper() and i else char
                       for i, char in enumerate(name))

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self._processors:
            print("No processor found, no data")
            return
        for proc in self._processors:
            label = self._camel_case_closed(proc.__class__.__name__)
            print(
                f"{label}: "
                f"total {proc.total_processed} items processed, "
                f"remaining {proc.remaining} on processor"
            )


def main() -> None:
    print("=== Code Nexus - Data Stream ===")

    print("\nInitialize Data Stream...")
    data_stream: DataStream = DataStream()
    data_stream.print_processors_stats()

    print("\nRegistering Numeric Processor")
    numeric_processor: NumericProcessor = NumericProcessor()
    data_stream.register_processor(numeric_processor)

    batch: list[Any] = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {
                "log_level": "WARNING",
                "log_message": "Telnet access! Use ssh instead",
            },
            {
                "log_level": "INFO",
                "log_message": "User wil is connected",
            },
        ],
        42,
        ["Hi", "five"],
    ]

    print(f"\nSend first batch of data on stream: {batch}")
    data_stream.process_stream(batch)
    data_stream.print_processors_stats()

    print("\nRegistering other data processors")
    text_processor: TextProcessor = TextProcessor()
    log_processor: LogProcessor = LogProcessor()
    data_stream.register_processor(text_processor)
    data_stream.register_processor(log_processor)

    print("Send the same batch again")
    data_stream.process_stream(batch)

    data_stream.print_processors_stats()

    print(
        "\nConsume some elements from the data processors: "
        "Numeric 3, Text 2, Log 1"
    )
    for _ in range(3):
        numeric_processor.output()
    for _ in range(2):
        text_processor.output()
    log_processor.output()

    data_stream.print_processors_stats()


if __name__ == "__main__":
    main()
