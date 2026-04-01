#!/usr/bin/env python3
# Heatmap visualization of phonetic similarity

import json
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from phonetic_similarity import compare


def main():
    candidates = [
        "dazona", "eluzor", "nashida", "zoyan", "bahnoz", "halima", "yazur",
        "yahwa", "iaou", "yawu", "yāū"
    ]
    rows = compare(candidates)
    df = pd.DataFrame(rows)
    df = df.set_index("candidate")
    plt.figure(figsize=(10, 6))
    sns.heatmap(df, annot=True, cmap="YlGnBu", fmt=".2f")
    plt.title("Triadic Names vs Reference Divine Names")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
