# C64 Mega Demo — Berlin 3SID journey

A Commodore 64 demo built on the U83R 3SID megademo engine and reworked into a
continuous audiovisual trip from Berlin Brandenburg Airport to the Golden
Heart Hotel.

The implementation lives in `src/subway.s`; its historical name reflects the
Berlin narrative, while the project retains the U83R multi-effect engine,
raster scheduler, and three-SID music system.

## Features

- 28 linked visual parts: title cards, digital rain, horizon warp, starfields,
  tunnel sequences, a wire cube, scrollers, and station transitions.
- Five evolving techno sections at approximately 150 BPM, with a distinct
  bass, melody, and drum SID at `$d400`, `$d420`, and `$d440` respectively.
- A deterministic raster IRQ and effect scheduler designed for a full
  multi-minute loop rather than an isolated screen.

## Build

Requirements:

- [ACME](https://sourceforge.net/projects/acme-crossass/), the 6502 assembler
- A C64 emulator such as VICE for running the generated PRG

```sh
./build_release.sh
```

The build writes `build/subway_3sid_v60.prg`.

## Run

Configure the emulator for three SID chips at `$d400`, `$d420`, and `$d440`,
then autostart the generated PRG. With VICE's `x64sc`, a typical command is:

```sh
x64sc -autostartprgmode 1 -autostart build/subway_3sid_v60.prg
```

## Verification

The repository includes a SHA-256 manifest for the source and release
metadata:

```sh
shasum -a 256 -c SHA256SUMS.txt
```

The supplied manifest and build are also used by the release workflow.

## Project notes

- [SUBWAY.md](SUBWAY.md) describes the Berlin composition and 3SID mix.
- [V6_0_0_NOTES.md](V6_0_0_NOTES.md) records the musical arrangement.
- [docs/LINEAGE.md](docs/LINEAGE.md) documents the archive/source naming
  mismatch and why this repository is categorized by implementation identity.

