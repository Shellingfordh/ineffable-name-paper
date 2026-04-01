# Ineffable Name Paper

This repo includes:
- `PAPER.md` — main paper + appended triadic phonosemantic language framework
- `code/` — Python tools for triadic generation, similarity scoring, breath modeling, and visualization

## Quick start

```bash
python3 code/triadic_generator.py > data/top_candidates.json
python3 code/phonetic_similarity.py > data/phonetic_scores.json
python3 code/breath_model.py
python3 code/triadic_cli.py --top 20
python3 code/visualize_similarity.py
```

## Note
All phonosemantic outputs are heuristic and exploratory.
