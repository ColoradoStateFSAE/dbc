import subprocess
import os
from pathlib import Path

OUTPUT = "nemesis.dbc"
DBC_DIR = "../dbc"
TEMP_OUTPUT = "nemesis_temp.dbc"

# Delete nemesis.dbc if it exists
if os.path.exists(OUTPUT):
    os.remove(OUTPUT)

# Merge all .dbc files
dbc_files = sorted(Path(DBC_DIR).glob("*.dbc"))
for dbc_file in dbc_files:
    if os.path.exists(OUTPUT):
        print(f"Merging {dbc_file} into {OUTPUT}...")
        subprocess.run(["canconvert", f"--merge={dbc_file}", OUTPUT, OUTPUT])
    else:
        print(f"Creating {OUTPUT} from {dbc_file}...")
        subprocess.run(["canconvert", str(dbc_file), OUTPUT])

# Remove FD frames
print(f"\nRemoving FD frames from {OUTPUT}...")
subprocess.run(["canconvert", "--unsetFrameFd=*", OUTPUT, TEMP_OUTPUT])

# Replace original with cleaned version
os.remove(OUTPUT)
os.rename(TEMP_OUTPUT, OUTPUT)

print(f"Done! Result: {OUTPUT} (all FD frames removed)")
