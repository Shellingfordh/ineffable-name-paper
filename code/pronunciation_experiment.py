#!/usr/bin/env python3
"""Pronunciation experiment runner for Divina Vox.

Generates timed inhale/hold/exhale/void prompts and optionally
speaks them on macOS using `say`.
"""

import argparse
import shutil
import sys
import time

DEFAULTS = {
    "inhale": 2.0,
    "hold": 1.0,
    "exhale": 3.0,
    "void": 1.5,
}


def say(text: str) -> None:
    """Speak text on macOS if `say` is available."""
    if shutil.which("say") is None:
        return
    # use a neutral voice; user can override via shell alias if desired
    import subprocess
    subprocess.run(["say", text], check=False)


def prompt(label: str, seconds: float, speak: bool) -> None:
    msg = f"{label.upper():<7} {seconds:>4.1f}s"
    print(msg)
    if speak:
        say(label)
    time.sleep(seconds)


def run_cycle(phrase: str, cycles: int, breath_only: bool, timings, speak: bool) -> None:
    for i in range(1, cycles + 1):
        print(f"\nCycle {i}/{cycles}")
        prompt("inhale (y)", timings["inhale"], speak)
        prompt("hold (h)", timings["hold"], speak)
        if not breath_only:
            if speak:
                say(phrase)
            print(f"EXHALE  {timings['exhale']:>4.1f}s  phrase: {phrase}")
        else:
            print(f"EXHALE  {timings['exhale']:>4.1f}s  phrase: [breath only]")
        time.sleep(timings["exhale"])
        prompt("void (w)", timings["void"], speak)


def main() -> int:
    parser = argparse.ArgumentParser(description="Divina Vox pronunciation experiment")
    parser.add_argument("--phrase", default="Yau", help="phrase to speak on exhale")
    parser.add_argument("--cycles", type=int, default=3, help="number of cycles")
    parser.add_argument("--breath-only", action="store_true", help="no phrase, breath cadence only")
    parser.add_argument("--inhale", type=float, default=DEFAULTS["inhale"], help="inhale seconds")
    parser.add_argument("--hold", type=float, default=DEFAULTS["hold"], help="hold seconds")
    parser.add_argument("--exhale", type=float, default=DEFAULTS["exhale"], help="exhale seconds")
    parser.add_argument("--void", type=float, default=DEFAULTS["void"], help="void seconds")
    parser.add_argument("--say", action="store_true", help="use macOS say for audio prompts")

    args = parser.parse_args()

    timings = {
        "inhale": args.inhale,
        "hold": args.hold,
        "exhale": args.exhale,
        "void": args.void,
    }

    if args.say and shutil.which("say") is None:
        print("Warning: --say requested but `say` not found; running silently.")

    run_cycle(args.phrase, args.cycles, args.breath_only, timings, args.say)
    print("\nDone.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
