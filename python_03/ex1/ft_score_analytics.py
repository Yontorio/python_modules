#!/usr/bin/env python3

import sys


def main() -> None:
    print("=== Player Score Analytics ===")
    scores: list[int] = []
    for arg in sys.argv[1:]:
        try:
            scores.append(int(arg))
        except ValueError:
            print(f"Invalid parameter: '{arg}'")
    if not scores:
        print("No scores provided. Usage: python3"
              " ft_score_analytics.py <score1> <score2> ...")
        return
    count: int = len(scores)
    total: int = sum(scores)
    average: float = total / count
    high: int = max(scores)
    low: int = min(scores)
    print(f"Scores processed: {scores}")
    print(f"Total players: {count}")
    print(f"Total score: {total}")
    print(f"Average score: {average}")
    print(f"High score: {high}")
    print(f"Low score: {low}")
    print(f"Score range: {high - low}")


if __name__ == "__main__":
    main()
