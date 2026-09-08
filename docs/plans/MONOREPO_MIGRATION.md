# Monorepo migration plan

## Target structure

```text
apps/web       Existing static web delivery wrapper
apps/mobile    Expo SDK 57 application
packages/content  Generated, shared evidence dataset
public         Current production web artifact
scripts        Content generation and validation harness
```

The first migration stage deliberately leaves the proven web artifact and Python research pipeline in place. Moving them into `apps/web` before mobile parity would create avoidable deployment risk. The root npm workspace already makes this a functional monorepo; a later physical move should occur only after the hosting configuration and redirects are captured in CI.

## Build flow

1. `npm run content:build` regenerates the canonical web data and syncs it into `packages/content`.
2. Both apps consume the same generated claims and evidence statuses.
3. `npm run audit` validates content, generated pages, internal links, and web behavior.
4. `npm run mobile:check` creates an Expo web export as a compilation gate.

## Migration gates

- Do not introduce a second biography source of truth.
- Do not move `public/` until the Cloudflare Pages build command and output directory are versioned.
- Do not enable EAS submission until bundle identifiers, store ownership, privacy answers, screenshots, icons, and credentials are approved.
- Do not describe the content corpus as complete while declared research gaps remain.
