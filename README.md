# news-image-20261120 — Friday 20 November 2026 in one image

A program that writes one image summing up Friday 20 November 2026's world
news to `/output/entry.png` (1024x1024 PNG, <1 MiB, deterministic, no network).

## How it works

- `draw_frontpage.py` renders the front page with PIL: a light masthead
  ("THE WORLD IN ONE DAY"), a BY THE NUMBERS strip (6 stats), a coloured
  region bar (36 stories across 7 regions), 3 illustrated heroes
  (Cyclone Akvan landfall in Odisha, Russian missiles hitting three Kyiv
  bridges, the Asian AI sell-off), 10 illustrated medium stories in a
  5x2 grid, a solid landmass world map, an ALSO list of 23 more stories,
  and a DATE CHECK naming Thursday 19 November stories deliberately
  left out.
- `main.py` copies the rendered `entry.png` to `/output/entry.png`.
- All art is procedural (drawn with PIL) except `worldmap.png`, the
  equirectangular base map recoloured at render time; no network.

## Stories (36)

Heroes: Cyclone Akvan (370,000 evacuated, Gopalpur landfall), Kyiv bridges
hit (3 killed, 2 in Lviv), Asian markets fall (Taiex -6.8%, Kospi -5.4%,
Nikkei -4.9%). Medium: COP31 final day, GTA VI first full day, Senate
Iran war-powers 51-48, Phillips 118, Senegal boat, Tonga drought, Pete
Rose pardon, Anthropic after-hours slide, Europe Ukraine talks, Nvidia
probe. Plus 23 more in ALSO.

## License

MIT. See LICENSE.
