# Ineffable Name Paper

This repo includes:
- `PAPER.md` — main paper + appended triadic phonosemantic language framework
- `code/` — Python tools for triadic generation, similarity scoring, breath modeling, pronunciation experiments, and visualization

## Quick start

```bash
python3 code/triadic_generator.py > data/top_candidates.json
python3 code/phonetic_similarity.py > data/phonetic_scores.json
python3 code/breath_model.py
python3 code/triadic_cli.py --top 20
python3 code/visualize_similarity.py
```

## Pronunciation experiment

Timed inhale/hold/exhale/void prompts with optional macOS audio:

```bash
python3 code/pronunciation_experiment.py --cycles 3 --phrase "Yau"
python3 code/pronunciation_experiment.py --cycles 3 --phrase "Iaou"
python3 code/pronunciation_experiment.py --cycles 3 --phrase "YHWH" --breath-only
# macOS voice prompts
python3 code/pronunciation_experiment.py --cycles 2 --phrase "Yau" --say
```

## Note
All phonosemantic outputs are heuristic and exploratory.
