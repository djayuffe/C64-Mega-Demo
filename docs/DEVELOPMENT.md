# Development guide

## Build targets

Run `make` to run the static audit and assemble `build/c64-mega-demo-3sid.prg`.
Run `make verify` to also verify the committed SHA-256 release manifest. Use
`make clean` to remove only the generated `build/` directory.

## Runtime architecture

| Area | Responsibility |
| --- | --- |
| `src/subway.s` | BASIC loader, VIC setup, IRQ, 3SID score, 28 renderers, and transitions. |
| `InitTbl` / `UpdateTbl` | The matching 28-part lifecycle dispatch tables. |
| `TV_PlayMusic` | IRQ-driven musical timing and the 3SID score. |
| `ThreeSIDEffectPolish` | Colour response derived from bass, melody, and drum pulses. |
| `ic_*`, `gt_*`, `cv_*`, `nw_*` | Corridor, trench, Cube V3, and wire-cube renderers. |
| `tools/static_audit.py` | Dispatch, asset, target-resolution, and VIC-state regression checks. |

## 3SID configuration

The program writes to three chips at `$d400`, `$d420`, and `$d440`. In VICE,
use two extra SIDs at those addresses:

```sh
x64sc -sidextra 2 -sid2address 0xd420 -sid3address 0xd440 \
  -autostartprgmode 1 -autostart build/c64-mega-demo-3sid.prg
```

The visual program will run with a one-SID configuration, but the intended
score requires the three-chip layout.

## Invariants

- `NUM_PARTS`, both dispatch tables, and all timing tables must contain 28
  entries in the same order.
- The program must remain below `$c000`; ACME enforces this at assembly time.
- The wire-cube binary assets are required at assembly time.
- The effect suite is intentionally continuous: the card and scroller routines
  are dormant in this release, so documentation must not describe visible cards
  or a running scroller.
