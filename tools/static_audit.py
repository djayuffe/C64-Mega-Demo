#!/usr/bin/env python3
"""Fast release gate for the C64 Mega Demo assembly source."""

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "src" / "subway.s"
TEXT = SOURCE.read_text(encoding="utf-8")
errors: list[str] = []


def fail(message: str) -> None:
    errors.append(message)


def table_count(label: str, directive: str) -> int:
    match = re.search(
        rf"^{re.escape(label)}\s*:?(.*?)(?=^[A-Za-z_][A-Za-z0-9_]*\s*:?(?:\s+!|:)|\Z)",
        TEXT,
        re.M | re.S,
    )
    if not match:
        fail(f"missing {label}")
        return -1
    values: list[str] = []
    for line in match.group(1).splitlines():
        directive_match = re.search(rf"!{directive}\s+(.+?)(?:;.*)?$", line)
        if directive_match:
            values.extend(item.strip() for item in directive_match.group(1).split(",") if item.strip())
    if not values:
        fail(f"{label} has no !{directive} values")
    return len(values)


parts_match = re.search(r"^NUM_PARTS\s*=\s*(\d+)", TEXT, re.M)
parts = int(parts_match.group(1)) if parts_match else -1
if parts != 28:
    fail(f"NUM_PARTS={parts}, expected 28")

for table in ("PartBorderTbl", "PartBgTbl", "PartFramesTbl_Lo", "PartFramesTbl_Hi", "PartBarsTbl"):
    count = table_count(table, "byte")
    if count != parts:
        fail(f"{table} has {count} entries, expected {parts}")
for table in ("InitTbl", "UpdateTbl"):
    count = table_count(table, "word")
    if count != parts:
        fail(f"{table} has {count} entries, expected {parts}")

for required in (
    "SID1       = $d400",
    "SID2       = $d420",
    "SID3       = $d440",
    "MegaMain_IRQ:",
    "ThreeSIDEffectPolish:",
    "!if * > $c000",
    "!text \"2061\"",
    "START_PART = 0",
    "lda #START_PART",
    "WireCubeChars:   !binary \"wire_cube_chars.bin\"",
    "WireCubeMask:    !binary \"wire_cube_mask.bin\"",
):
    if required not in TEXT:
        fail(f"missing required runtime marker: {required}")

# The appended effects must actually drive VIC state; loading a palette value
# without writing it silently left their presentation at a prior scene's state.
for required in (
    "lda NfxCoolPalette,x\n        sta BORDER\n        lda #$00\n        sta BKG",
    "ora #$08\n        sta scrollReg",
    "lda NfxCorridorBg,x\n        sta BKG\n        lda NfxCorridorBorder,x\n        sta BORDER",
    "lda NfxGoldBorder,x\n        sta BORDER\n        lda #$00\n        sta BKG",
):
    if required not in TEXT:
        fail("missing new-effect VIC state write")

defined = set(re.findall(r"^([A-Za-z_][A-Za-z0-9_@]*)\s*:", TEXT, re.M))
constants = set(re.findall(r"^([A-Za-z_][A-Za-z0-9_]*)\s*=", TEXT, re.M))
external = {"KERNAL_IRQ"}
for operation, target in re.findall(r"\b(jsr|jmp)\s+([A-Za-z_][A-Za-z0-9_@]*)\b", TEXT):
    if target.startswith("@"):
        continue
    if target not in defined and target not in constants and target not in external:
        fail(f"undefined global {operation.upper()} target: {target}")

for asset in (ROOT / "src" / "wire_cube_chars.bin", ROOT / "src" / "wire_cube_mask.bin"):
    if not asset.is_file() or asset.stat().st_size == 0:
        fail(f"missing or empty binary asset: {asset.name}")

if errors:
    print("STATIC AUDIT FAILED")
    for error in errors:
        print(f" - {error}")
    sys.exit(1)

print("STATIC AUDIT OK")
print("28-part dispatch and timing tables match")
print("3SID map $d400/$d420/$d440 verified")
print("effect VIC state writes and binary assets verified")
print("global JSR/JMP target guard present")
