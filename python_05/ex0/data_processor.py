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


def main() -> None:
    print("=== Code Nexus - Data Processor ===")

    print("\nTesting Numeric Processor...")
    np = NumericProcessor()
    print(f"Trying to validate input '42': {np.validate(42)}")
    print(f"Trying to validate input 'Hello': {np.validate('Hello')}")
    print(
        "Test invalid ingestion of string 'foo' "
        "without prior validation:"
    )
    try:
        np.ingest("foo")
    except ValueError as e:
        print(f"Got exception: {e}")

    print("Processing data: [1, 2, 3, 4, 5]")
    np.ingest([1, 2, 3, 4, 5])
    print("Extracting 3 values...")
    for _ in range(3):
        rank, value = np.output()
        print(f"Numeric value {rank}: {value}")

    print("\nTesting Text Processor...")
    tp = TextProcessor()
    print(f"Trying to validate input '42': {tp.validate(42)}")
    print("Processing data: ['Hello', 'Nexus', 'World']")
    tp.ingest(["Hello", "Nexus", "World"])
    print("Extracting 1 value...")
    rank, value = tp.output()
    print(f"Text value {rank}: {value}")

    print("\nTesting Log Processor...")
    lp = LogProcessor()
    print(f"Trying to validate input 'Hello': {lp.validate('Hello')}")
    log_data: list[dict[str, str]] = [
        {
            "log_level": "NOTICE",
            "log_message": "Connection to server",
        },
        {
            "log_level": "ERROR",
            "log_message": "Unauthorized access!!",
        },
    ]
    print(f"Processing data: {log_data}")
    lp.ingest(log_data)
    print("Extracting 2 values...")
    for _ in range(2):
        rank, value = lp.output()
        print(f"Log entry {rank}: {value}")


if __name__ == "__main__":
    main()
