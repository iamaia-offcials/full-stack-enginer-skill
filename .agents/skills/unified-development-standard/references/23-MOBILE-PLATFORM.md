# 23. Mobile and desktop applications, platform integration

- `[MOB-001] MUST` Separate platform UI/OS APIs (Android/iOS/Windows/macOS) from the domain core and backend contracts. Follow platform UX guidance while keeping brand consistency.
- `[MOB-002] MUST` Store access credentials in platform-secure storage where applicable. A public client cannot protect server secrets; servers enforce permissions for their resources.
- `[MOB-003] MUST` Evolve backend contracts with delayed mobile-client updates in mind. Do not break installed builds through an abrupt API change.
- `[MOB-004] MUST` Handle offline/poor connectivity, foreground/background lifecycle, retries, and form preservation without unexpected duplicate operations.
- `[MOB-005] MUST` For distributed application builds, sign and publish through a secure pipeline with scoped secrets. Separate staging/beta channels from production.
- `[MOB-006] SHOULD` Test applicable platform differences: permissions, deep links, notifications, accessibility, dynamic text, hardware keyboards, supported themes, and screen sizes.
- `[MOB-007] MUST` Control collected telemetry, permissions, and disclosures; meet applicable store/OS requirements. Recheck changing platform policies before release.

Mobile UI may use different navigation patterns on iOS and Android while sharing domain/API behavior. Docker/Podman can support backend/CI; **containers are not a required mobile-app distribution format**.

## Supported mobile modes and optimization
- `[MOB-008] MUST` Distinguish native Android/iOS, cross-platform, PWA, Telegram Mini App, and mobile web in the project profile. Store-publication rules do not apply to ordinary websites.
- `[MOB-009] MUST` Account for safe areas, software keyboards, dynamic text, orientation, touch, supported system themes, and offline/interrupted flows on supported platforms.
- `[MOB-010] MUST` Recover from foreground/background changes, kill/restart, and lost connectivity without losing critical data or creating duplicate transactions.
- `[MOB-011] MUST` Server API changes account for installed clients with delayed updates; document supported versions and deprecation windows.
- `[MOB-012] SHOULD` Profile startup, scrolling/jank, memory, network activity, and energy on physical devices. Android Baseline Profiles and Apple Instruments are examples only for their respective platforms.
- `[MOB-013] MUST` Verify signing, keys, permissions, deep links, and notifications for the actual features, with minimum privileges and applicable user consent.
- `[MOB-014] MUST` Before release, maintain a device/OS compatibility matrix that identifies untested combinations. Emulator results do not prove identical physical-device behavior.
- `[MOB-015] SHOULD` Apply web/SEO/performance rules to mobile web and PWA according to purpose. Do not add service workers, offline support, or app manifests merely to call a site an application.
