# Complete effect gallery

Every row below is one entry in the production `InitTbl`/`UpdateTbl` dispatch.
The image is a native 384×272 VICE capture of that renderer running in the
three-SID build. The first 15 captures were produced with the deterministic
`START_PART` review selector; the remaining frames were captured from the same
PRG at their corresponding sequence windows. They are visual evidence of the
shipped renderers, not concept art.

| # | Effect | Description | Runtime screenshot |
|---:|---|---|---|
| 0 | 3SID Pulse Field | Opening colour field driven by the shared bass, melody, and drum pulse envelopes. | ![3SID Pulse Field](screenshots/effects/effect-0.png) |
| 1 | Plasma Storm | Interfering phase tables write a continuously changing plasma colour surface. | ![Plasma Storm](screenshots/effects/effect-1.png) |
| 2 | Hyperspace | Centre-out fixed-point star motion accelerates toward the viewer. | ![Hyperspace](screenshots/effects/effect-2.png) |
| 3 | XOR Moire | Sharp XOR interference bands form high-contrast rotating diamond patterns. | ![XOR Moire](screenshots/effects/effect-3.png) |
| 4 | Waves | Sine-displaced horizontal colour bands sweep across the text-mode field. | ![Waves](screenshots/effects/effect-4.png) |
| 5 | Tunnel | A forward-moving colour tunnel uses depth and yaw phases without self-modifying code. | ![Tunnel](screenshots/effects/effect-5.png) |
| 6 | Sine Starfield | Fast and slow star populations drift in parallax while their colours pulse. | ![Sine Starfield](screenshots/effects/effect-6.png) |
| 7 | Text Wireframe | A row-safe text-mode wireframe grid adapts cube geometry to the character screen. | ![Text Wireframe](screenshots/effects/effect-7.png) |
| 8 | Heart Voyager Trail | A heart silhouette receives a moving voyager trail and halo treatment. | ![Heart Voyager Trail](screenshots/effects/effect-8.png) |
| 9 | Multiplex Cube | Alternating horizontal and vertical edge bars evoke sprite-multiplex timing in text mode. | ![Multiplex Cube](screenshots/effects/effect-9.png) |
| 10 | Yaw Wobble Tunnel | A tunnel variant applies deterministic column wobble and per-cell tint. | ![Yaw Wobble Tunnel](screenshots/effects/effect-10.png) |
| 11 | Turbo Boot Tunnel | A high-energy boot-grid tunnel uses automatic text-mode zoom phases. | ![Turbo Boot Tunnel](screenshots/effects/effect-11.png) |
| 12 | Golden Halo Heart | A distinct golden animated halo surrounds the heart form. | ![Golden Halo Heart](screenshots/effects/effect-12.png) |
| 13 | Raster Grid Boot | Layered grid rows and raster colour changes create a boot-up field. | ![Raster Grid Boot](screenshots/effects/effect-13.png) |
| 14 | Cyber Grid | A neon matrix-floor adaptation combines grid geometry with music colour response. | ![Cyber Grid](screenshots/effects/effect-14.png) |
| 15 | Safe Tunnel Prime | A conservative tunnel renderer with bounded arithmetic and stable row ownership. | ![Safe Tunnel Prime](screenshots/effects/effect-15.png) |
| 16 | Black Orbit Field | Orbital rings fold around a dark centre to create a black-hole impression. | ![Black Orbit Field](screenshots/effects/effect-16.png) |
| 17 | Rotor Cube Final | A corrected 16-step rotating cube uses projected front/back rectangles and sparse connectors. | ![Rotor Cube Final](screenshots/effects/effect-17.png) |
| 18 | Solar Flare | A radial flare renderer expands bright colour energy from a central origin. | ![Solar Flare](screenshots/effects/effect-18.png) |
| 19 | Prism Gate | Layered gate bars open and close around a colour-shifting central passage. | ![Prism Gate](screenshots/effects/effect-19.png) |
| 20 | Twist Lattice | Interleaved lattice lines twist through phase-shifted character and colour tables. | ![Twist Lattice](screenshots/effects/effect-20.png) |
| 21 | Infinity Corridor | Distance tables, column warp, and palette cycling form an endless corridor. | ![Infinity Corridor](screenshots/effects/effect-21.png) |
| 22 | Gold Trench | Perspective rails, inner glow, vanishing markers, and beat crossbars draw a gold trench. | ![Gold Trench](screenshots/effects/effect-22.png) |
| 23 | Cube V3 Rotor | A stable 3D wire cube draws front/rear planes, corner joints, and independent depth connectors. | ![Cube V3 Rotor](screenshots/effects/effect-23.png) |
| 24 | Vortex | Precomputed angle/distance fields rotate a dense colour vortex around the screen. | ![Vortex](screenshots/effects/effect-24.png) |
| 25 | Mux Edge Field | Alternating edge bands convert sprite-multiplex timing ideas into safe character geometry. | ![Mux Edge Field](screenshots/effects/effect-25.png) |
| 26 | Raster Boot Tunnel | A raster-synchronised boot tunnel builds depth with bounded row and phase tables. | ![Raster Boot Tunnel](screenshots/effects/effect-26.png) |
| 27 | Wire Cube Clean | Mirrored moving wire accents close the sequence with a sparse cube-grid motif. | ![Wire Cube Clean](screenshots/effects/effect-27.png) |

## Reproduction

The selector is an assembler-time review aid and does not change the normal
release start (part 0):

```sh
cd src
acme -DSTART_PART=23 -f cbm -o ../build/review-effect-23.prg subway.s
x64sc -sidextra 2 -sid2address 0xd420 -sid3address 0xd440 \
  -autostartprgmode 1 -autostart ../build/review-effect-23.prg
```
