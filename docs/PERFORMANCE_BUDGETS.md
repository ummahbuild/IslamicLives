# Performance budgets

These budgets keep ordinary reading pages light while allowing the interactive atlas to use Three.js when requested.

| Surface | Budget | Current measurement |
| --- | ---: | --- |
| Initial shared JavaScript, CSS, and collection data | 60 KB gzip | Enforced by `scripts/check_performance.py` |
| Atlas-only code, map data, and Three.js modules | 260 KB gzip | Lazy-loaded and enforced separately |
| Largest generated HTML page | 15 KB uncompressed | Enforced across every generated route |
| Primary interaction response | 100 ms target | Requires browser/device telemetry before it can become a CI assertion |
| Animation | 60 fps target | Requires representative device profiling |

The compressed figures are deterministic local estimates, not substitutes for field measurements. CI also verifies that the atlas is absent from the initial JavaScript module graph. Network, parsing, GPU, and device performance must be measured before a public performance claim is made.

The globe remains an enhancement: sourced atlas text and chapter routes are available without WebGL. Motion respects the existing reduced-motion treatment.
