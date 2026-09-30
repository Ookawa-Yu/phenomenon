# /// script
# requires-python = ">=3.10"
# dependencies = ["matplotlib"]
# ///

"""
Read the file in data/, make one picture, save it to out/.

    uv run plot.py

Three parts, and you will replace all three: rows() reads the file the way *your*
file needs reading, the loop in main() picks the numbers out of it, and the plot at
the bottom is the transformation you chose. Print before you plot.
"""

import csv
from datetime import datetime
from pathlib import Path


import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
DATA_FILE = HERE / "data" / "usgs-earthquakes-m8-since-1900.csv"


with DATA_FILE.open(encoding="utf-8-sig", newline="") as file:
    rows = list(csv.DictReader(file))

if not rows:
    raise ValueError("CSV no earhquake data found.")

print("first record：", rows[0])

raw_magnitude = rows[0]["mag"]
print("level：", raw_magnitude)
print("type：", type(raw_magnitude))

magnitude = float(raw_magnitude)
print("convert to level：", magnitude)
print("convert to type：", type(magnitude))


times = [
    datetime.fromisoformat(row["time"].replace("Z", "+00:00"))
    for row in rows
]
magnitudes = [float(row["mag"]) for row in rows]


fig, ax = plt.subplots(figsize=(10, 5))
ax.scatter(times, magnitudes, color="steelblue", s=65)

ax.set_title("USGS earthquakes: M8+ since 1900 (selected region)")
ax.set_xlabel("Year (UTC)")
ax.set_ylabel("Magnitude")
ax.grid(True, alpha=0.3)

fig.tight_layout()


output = HERE / "out" / "earthquakes.png"
output.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(output, dpi=200)
print("Pic has been saved to：", output)

plt.show()
