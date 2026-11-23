# Video Mask Timeline

Summarize object presence and mask size over video frames.

## What this project does

This is an original command-line utility for analyzing or presenting computer vision outputs. It does not include pretrained weights, training code, or copied research implementations.

## Input and output

Input example: `[{"object_id":1,"frame":0,"pixels":1530}]`

Run: `python main.py masks.json timeline.csv`

See `python main.py --help` for positional arguments. Output is written to the requested file, except the neighbor search, which prints ranked results.

## Related tools

SAM 2 or another video segmentation exporter. This project is independent of those implementations and consumes their exported results where applicable.

## Requirements

Python 3.10 or newer. No third-party Python packages are required.

## Limitations

Each record needs object_id, frame, and mask pixel count. Model inference is not locally tested. The utility has only been checked for syntax and on small synthetic inputs.


## Why it is useful

Video segmentation systems can lose objects over time. This tool summarizes the frames where each object has a mask and the average area of those masks. The resulting table is a starting point for reviewing object persistence.

## Data contract

Input is a JSON array of `{object_id, frame, pixels}` records. `frame` is an integer index and `pixels` is the mask area. Output has first and last observed frame, number of observed frames, and mean mask pixels for each object.

## Reproduce the example

```bash
python main.py examples/masks.json examples/timeline.csv
```

The command reads the included sample input. Generated reports in `examples/` can be removed when finished.

## Interpretation

Observed frames may have gaps. The report does not infer missing frames, assess mask quality, or compare against ground truth.

## License

MIT. See `LICENSE`.

