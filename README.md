# news-image-20261120 — Friday 20 November 2026 in one image

A program that writes one image summing up Friday 20 November 2026's world
news to `/output/entry.png` (1024x1024 PNG, <1 MiB, deterministic, no network).

## How it works

- `draw_frontpage.py` renders the front page with PIL: a navy-and-gold
  masthead ("THE WORLD IN ONE DAY"), a region bar (36 stories across 7
  regions), a UTC strip, 3 illustrated heroes (Cyclone Akvan landfall in
  Odisha, Russian missiles hitting three Kyiv bridges, the Asian AI
  sell-off), 12 illustrated medium stories, a BY THE NUMBERS strip, a
  world map, an ALSO list of 21 more stories, and a DATE CHECK naming
  Thursday 19 November stories deliberately left out.
- `main.py` copies the rendered `entry.png` to `/output/entry.png`.
- All art is procedural (drawn with PIL); no external images, no network.

## Stories (36)

Heroes: Cyclone Akvan (370,000 evacuated, Gopalpur landfall), Kyiv bridges
hit (3 killed, 2 in Lviv), Asian markets fall (Taiex -6.8%, Kospi -5.4%,
Nikkei -4.9%). Medium: COP31 final day, GTA VI first full day, Senate
Iran war-powers 51-48, Phillips 118, Senegal boat, Tonga drought, Pete
Rose pardon, Anthropic after-hours slide, Europe Ukraine talks, Nvidia
probe, Cyclone Xavier, Nicholls 175*. Plus 21 more in ALSO.

## License

MIT. See LICENSE.
