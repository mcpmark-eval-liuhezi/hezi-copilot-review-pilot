#!/usr/bin/env python3
"""pilot_change.py — Example script for the Copilot code review pilot."""

def add(a: int, b: int) -> int:
    """Return the sum of two integers."""
    return a + b


def main() -> None:
    result = add(2, 3)
    print(f"add(2, 3) = {result}")


if __name__ == "__main__":
    main()
