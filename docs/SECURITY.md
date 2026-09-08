# Security and dependency posture

Reviewed: 2026-09-08

- The static web app has no accounts, form submission, server-side database, or runtime secret surface.
- Production headers deny framing, objects, camera, microphone, and geolocation; restrict scripts, styles, images, and network connections; and enable HSTS.
- The Expo application bundles read-only public content and requests no device permissions.
- `npm audit --omit=dev` currently reports ten moderate transitive findings within Expo CLI/config tooling, including the `xcode` → `uuid` chain. It reports no high or critical findings.
- npm proposes Expo 46 as the available automatic remediation. That would be a major unsupported downgrade from SDK 57 and must not be applied. Recheck after each Expo 57 patch and upgrade when Expo publishes a compatible remediation.
- Use Node 24 LTS. Node 23 is outside React Native 0.86’s supported engine range.

Security reports should not include private user data or credentials. The public correction/support address must be selected before store launch.
