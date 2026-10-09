import csv
import sys
from collections import Counter

ALLOWED_LABELS = {"positive", "negative", "neutral"}

def run(path):
    with open(path, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    ids = [r.get("record_id", "").strip() for r in rows]
    duplicate_ids = sum(v > 1 for v in Counter(ids).values())

    invalid_labels = sum(r.get("label", "").strip() not in ALLOWED_LABELS for r in rows)
    missing_text = sum(not r.get("text", "").strip() for r in rows)

    bad_confidence = 0
    for row in rows:
        try:
            score = float(row.get("confidence", ""))
            if not 0 <= score <= 1:
                bad_confidence += 1
        except ValueError:
            bad_confidence += 1

    print("\nANNOTATION QA")
    print("-" * 13)
    print(f"Records:          {len(rows)}")
    print(f"Invalid labels:   {invalid_labels}")
    print(f"Missing text:     {missing_text}")
    print(f"Bad confidence:   {bad_confidence}")
    print(f"Duplicate IDs:    {duplicate_ids}")

    issues = invalid_labels + missing_text + bad_confidence + duplicate_ids
    print(f"\nStatus: {'PASS' if issues == 0 else 'REVIEW REQUIRED'}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python qa_check.py <csv-file>")
        raise SystemExit(1)
    run(sys.argv[1])
