import argparse, csv, json
from collections import defaultdict

def timeline(records):
    groups = defaultdict(list)
    for row in records:
        groups[str(row["object_id"])].append((int(row["frame"]), int(row["pixels"])))
    return [{"object_id": obj, "first_frame": min(f for f, _ in values),
             "last_frame": max(f for f, _ in values), "observed_frames": len(values),
             "mean_mask_pixels": round(sum(p for _, p in values)/len(values), 2)}
            for obj, values in sorted(groups.items())]

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("input"); ap.add_argument("output"); a = ap.parse_args()
    rows = timeline(json.load(open(a.input, encoding="utf-8")))
    with open(a.output, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["object_id","first_frame","last_frame","observed_frames","mean_mask_pixels"])
        w.writeheader(); w.writerows(rows)
if __name__ == "__main__": main()

