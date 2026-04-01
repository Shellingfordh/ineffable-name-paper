#!/usr/bin/env python3
# Breath cycle model for sacred speech

from dataclasses import dataclass
from typing import List

@dataclass
class BreathPhase:
    name: str
    symbol: str
    description: str

PHASES = [
    BreathPhase("Inhale", "y", "connect/init"),
    BreathPhase("Hold", "h", "buffer/condition"),
    BreathPhase("Exhale", "el", "execute"),
    BreathPhase("Void", "w", "return/reset"),
]


def render_sequence(phrase: str) -> str:
    # Map a phrase into a 4‑phase breath guide
    return (
        f"Inhale({PHASES[0].symbol}) → {phrase}\n"
        f"Hold({PHASES[1].symbol}) → silent\n"
        f"Exhale({PHASES[2].symbol}) → execute\n"
        f"Void({PHASES[3].symbol}) → reset"
    )


def main():
    examples = [
        "Yaū Lira", "Eya Lira", "Saru Yaen Voro"
    ]
    for ex in examples:
        print("===")
        print(ex)
        print(render_sequence(ex))


if __name__ == "__main__":
    main()
