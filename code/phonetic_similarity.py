#!/usr/bin/env python3
# Phonetic similarity and position-weighted scoring

import itertools
import json
from difflib import SequenceMatcher

NAMES = ["YHWH", "Yahweh", "Allah", "Elohim", "Brahman", "Ehyeh", "Iao"]

# Position weights: start, middle, end
POSITION_WEIGHTS = [0.5, 0.3, 0.2]


def position_weighted_score(candidate: str, ref: str) -> float:
    cand = candidate.lower()
    ref = ref.lower()
    # split candidate into 3 chunks
    n = len(cand)
    if n < 3:
        return SequenceMatcher(None, cand, ref).ratio()
    parts = [cand[: n//3], cand[n//3: 2*n//3], cand[2*n//3:]]
    score = 0.0
    for w, p in zip(POSITION_WEIGHTS, parts):
        score += w * SequenceMatcher(None, p, ref).ratio()
    return score


def compare(candidates):
    rows = []
    for c in candidates:
        row = {"candidate": c}
        for r in NAMES:
            row[r] = round(position_weighted_score(c, r), 4)
        rows.append(row)
    return rows


def main():
    # Example triadic outputs
    candidates = [
        "dazona", "eluzor", "nashida", "zoyan", "bahnoz", "halima", "yazur",
        "yahwa", "iaou", "yawu", "yāū"
    ]
    rows = compare(candidates)
    print(json.dumps(rows, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
