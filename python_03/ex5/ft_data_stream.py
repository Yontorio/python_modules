#!/usr/bin/env python3

import random
from typing import Generator

PLAYERS: list[str] = ["alice", "bob", "charlie", "dylan"]
ACTIONS: list[str] = [
    "run", "eat", "sleep", "grab", "move", "crawl",
    "climb", "swim", "release", "use", "jump", "catch",
    "throw", "push", "pull", "drink", "kick", "bite",
    "scratch", "heal", "cast", "burn", "freeze", "explode",
    "walk", "dance", "sing", "cry", "laugh", "talk",
    "whisper", "shout", "scream", "fly"
]


def gen_event() -> Generator[tuple[str, str], None, None]:
    while True:
        yield (random.choice(PLAYERS), random.choice(ACTIONS))


def consume_event(events: list[tuple[str, str]]
                  ) -> Generator[tuple[str, str], None, None]:
    while events:
        yield events.pop(random.randint(0, len(events)-1))


def main() -> None:
    print("=== Game Data Stream Processor ===")

    gen: Generator[tuple[str, str], None, None] = gen_event()
    for i in range(1000):
        event: tuple[str, str] = next(gen)
        print(f"Event {i}: Player {event[0]} did action {event[1]}")

    event_list: list[tuple[str, str]] = [next(gen) for _ in range(10)]
    print(f"Built list of 10 events: {event_list}")
    for event in consume_event(event_list):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {event_list}")


if __name__ == "__main__":
    main()
