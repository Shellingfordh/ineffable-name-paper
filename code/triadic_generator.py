#!/usr/bin/env python3
# Triadic Phonosemantic Generator and Scorer

import itertools
import json
import math
from dataclasses import dataclass
from typing import Dict, List, Tuple

@dataclass
class Candidate:
    name: str
    void: str
    root: str
    force: str
    score: float
    scores: Dict[str, float]

# Phoneme banks (customizable)
VOID = ["ZO", "HA", "BA", "THA", "NA", "HH", "'A"]
ROOT = ["DA", "EL", "MA", "RA", "AN", "OR", "YA"]
FORCE = ["NA", "YA", "RA", "TA", "WA", "KA", "LA"]

# Reference divine names (phoneme approximations)
REFS = {
    "YHWH": ["Y", "H", "W", "H"],
    "Yahweh": ["YA", "WE"],
    "Allah": ["AL", "LA", "H"],
    "Elohim": ["EL", "O", "HIM"],
    "Brahman": ["BRA", "AH", "MAN"],
    "Ehyeh": ["EH", "YEH"],
}

# Phonosemantic weights by slot
SLOT_WEIGHTS = {"void": 0.35, "root": 0.4, "force": 0.25}

# Simple phonetic overlap scoring

def overlap_score(candidate: str, ref: List[str]) -> float:
    cand = candidate.lower()
    total = 0.0
    for part in ref:
        if part.lower() in cand:
            total += 1.0
    return total / max(len(ref), 1)


def triadic_candidates() -> List[Tuple[str, str, str, str]]:
    combos = itertools.product(VOID, ROOT, FORCE)
    return [(v, r, f, f"{v}-{r}-{f}") for v, r, f in combos]


def score_candidate(v: str, r: str, f: str) -> Dict[str, float]:
    name = f"{v}{r}{f}"
    scores = {}
    for k, ref in REFS.items():
        scores[k] = overlap_score(name, ref)
    return scores


def total_score(v: str, r: str, f: str, scores: Dict[str, float]) -> float:
    # slot bias: prefer lighter void, stronger root, active force
    slot_bias = {
        "void": 1.0 if v in ("HA", "HH", "'A") else 0.9,
        "root": 1.0 if r in ("EL", "YA", "AN") else 0.85,
        "force": 1.0 if f in ("YA", "WA", "RA") else 0.8,
    }
    base = (SLOT_WEIGHTS["void"] * slot_bias["void"] +
            SLOT_WEIGHTS["root"] * slot_bias["root"] +
            SLOT_WEIGHTS["force"] * slot_bias["force"])
    ref_score = sum(scores.values()) / max(len(scores), 1)
    return 0.6 * base + 0.4 * ref_score


def generate(top_n: int = 50) -> List[Candidate]:
    out: List[Candidate] = []
    for v, r, f, label in triadic_candidates():
        scores = score_candidate(v, r, f)
        score = total_score(v, r, f, scores)
        out.append(Candidate(label, v, r, f, score, scores))
    out.sort(key=lambda c: c.score, reverse=True)
    return out[:top_n]


def main():
    top = generate(50)
    rows = []
    for c in top:
        row = {
            "name": c.name,
            "void": c.void,
            "root": c.root,
            "force": c.force,
            "score": round(c.score, 4),
        }
        for k, v in c.scores.items():
            row[f"ref_{k}"] = round(v, 4)
        rows.append(row)
    print(json.dumps(rows, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
