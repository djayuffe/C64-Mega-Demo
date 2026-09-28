# Release audit

`make verify` is the local release gate. It runs `tools/static_audit.py`,
assembles with ACME strict segments, and checks the SHA-256 manifest.

The static audit validates:

- 28 matching entries in every dispatch and timing table;
- the three-SID address map at `$d400`, `$d420`, and `$d440`;
- the BASIC loader, IRQ, memory-ceiling guard, and required binary assets;
- resolved global `JSR`/`JMP` targets; and
- the VIC writes that set the Wire Cube, Infinity Corridor, and Gold Trench
  palette/background/fine-scroll state.

This source-structure gate complements a manual VICE smoke test. It does not
replace listening to the three-SID mix or visually checking timing-sensitive
raster behaviour.
