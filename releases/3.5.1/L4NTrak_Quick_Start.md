# L4NTrak 3.5.1 music hotfix

See RELEASE_3.5.1.md for fixes and device checks. In Live hub on Android, allow song information, play music in your music app, return and tap Refresh playback. Enable Live hub on both paired devices to display phone music on the PC. Remote control consent is separate. Trusted Wi-Fi/hotspot connections need no VPN app; separate-network internet still needs a private VPN.

# L4NTrak 3.5.0

Install the matching Android APK or Linux DEB over your existing app. Do not uninstall or clear app data.

To move your garage and photos, open Account & sharing on the device that has your files and choose **Export full account with images**. On the other device choose **Use existing account**, import the full ZIP and enter the account password. Android has a dedicated **Import full account ZIP with images** picker. Old identity-only JSON files contain no photos or vehicle files. Full ZIPs contain private vehicle data without file encryption; keep them private.

For ongoing PC–phone sync, sign in with the same imported identity on both devices. Open Wi-Fi & Bluetooth on the PC, enable its host and create a two-way pairing for your selected vehicles, or explicitly include all present/future vehicles. Save that pairing on Android and enable Auto Sync. **Sync now** receives missing allowed vehicles automatically. Keep both apps open on the same Wi-Fi/hotspot, or use paired Bluetooth. This is local device sync; signing in alone does not connect devices over the internet.

Both updated devices use verified disk-backed chunks for project ZIPs up to 150 MB (300 MB expanded; 20 MB per file). Independent edits pause for review. Matching project revisions can repair missing or corrupt attachments from a healthy peer without replacing records. Larger complete garages should be transferred as individual vehicle backups. The existing project backups, identity-only export and USB/shared-folder sync remain available.

The public, credential-free update feed is in Modzwastaken/l4ntrak-downloads. The source repository remains private. Android/Linux still ask for installation approval.


A local garage, workshop and driving companion for Android ARM64 and Linux. Vehicle records, photos, receipts and preferences are stored on your device. The account identity and project data can be transferred to your own other devices.

## Install the update

**Android bootstrap:** open the downloaded APK directly in Android Files / Downloads to install this hotfix. The older in-app file updater cannot receive its own native fix until the hotfix is installed.

Install **L4NTrak_3.4.2_Android.apk** over the existing Android app, or open **L4NTrak_3.4.2_all.deb** in your Linux package installer. Do not uninstall or clear data first. Android retains package `local.lancer.project` and the existing release signing certificate; Linux retains package `lancer-garage`. Complete the system installer prompts, then reopen the app. Export a project backup before a major change.

The source archive includes `run.sh`, the Python app, Android source and native runtime notices. Run `./run.sh` on a Linux system with the listed desktop dependencies. Building an APK requires the Android SDK, JDK and your own signing key; a different key cannot replace the existing signed installation. Signing secrets are excluded.

## What's new

The Android updater now selects, stages and hashes APKs from disk without sending full files through JavaScript/Base64. Public downloads and the pre-install backup also stream to disk. Manual token entry and Owner options are removed. See RELEASE_3.4.2.md for the hotfix and its test limits.

- Long song titles and artists stay inside the driving sheet. Previous, play/pause, next and the main controls remain reachable. Tap the song for full details.
- Nearby camera reports remain cached for ten minutes after coverage refreshes. A large red ring marks very close reports. Dashed rings show last-known reports when GPS is uncertain; live distance and proximity sound pause until GPS recovers.
- Route recalculation confirms deviation using distinct accurate GPS samples, then requests actual road routing. It preserves pending stops, omits passed stops and updates ETA. Failed requests retain the previous route and back off. Recalculate now is available in Directions, driving More and local Trak commands. Cached-only mode does not request a new route.
- Explore and the navigation menu share categories. Explore searches all standard pages and custom sections. Settings adds search, Show all, keyboard category navigation and automatic reveal of invalid fields. Long pages provide section jumps. Main navigation tabs avoid redundant Back buttons; nested menus and secondary pages keep their return controls.
- A fresh car-and-navigation icon is used across launchers and the app.
- Update checks distinguish a newer release, a matching release, an older feed and an unavailable feed. Unavailable downloads never prove the app is current.

## Find your way

Today, Maps, Garage, Trak and Explore are the main tabs. Explore groups Maps & travel, Garage & vehicle, Workshop, Insights & AI, and Settings & history. Quick access (star button or Alt+J) manages pinned pages, recent pages and reading comfort. Ctrl+K finds pages and saved records. Record editors, dialogs, map options and driving More have their own return controls.

Settings changes use Save customization. Camera and map toggles save immediately; project preferences travel with vehicle sync. System permissions, downloaded engines/models, temporary GPS and audio output remain device-local.

## Maps and driving

Allow location access, choose a destination or saved place, calculate a route and start guidance. Route and camera services can be incomplete or unavailable. OSRM routes do not include live traffic. An IP estimate is only an approximate area, not live driving GPS.

Driving view keeps turn guidance, speed, Recenter, Ask Trak, More and music together. More contains Directions, Recalculate route, map orientation, voice/music/camera setup and all map options. Map options is a scrollable sheet with a section chooser. GPS guidance trims the traveled route. Heading-up needs a usable GPS direction; a stationary fix may have none.

Camera alerts use loaded public reports near your GPS position, independently of map zoom or layer visibility. Enable Camera Alert and optional chime, then use Test chime to confirm output. Quiet Trak and camera sound are independent. Audio follows device media volume and output. A reported camera location does not confirm an active camera or access to private footage. Camera reports, public feeds and mapped speed limits may be incomplete or dated; observe actual signs and conditions.

Ask Trak is one question per tap in driving view. Listening does not restart automatically there. Quiet Trak offers typed commands without speech. Map and music commands such as north up, next turn, recalculate route, pause music and next track run directly where supported. General questions use the selected AI engine; model loading and reply speed depend on the device and installed model.

Music supports local audio and, on Android, controls for an active music app. Song information from other apps requires optional Android notification access. It reads active media metadata and does not save notification contents. Local music pauses when Maps leaves the foreground. Bluetooth output is selected through device audio settings.

## Garage and workshop

Garage manages multiple vehicles and their main photos, archives and showroom. Plans, work receipts, maintenance, parts, fuel, trips, events, evidence and custom sections belong to the active vehicle. Performance tools are estimates from entered values. The 3D showroom and Studio are visual planning tools; imported models require their own rigs and dimensions. AI drafts require review and Save before becoming project records.

App health offers a bounded set of session repairs and diagnostics. It cannot silently patch executable code or prove that every native feature works.

## Accounts, backup and sync

An account identity contains password-protected sign-in keys; it does not contain the vehicle project. Export the identity for your own devices, use the same password when importing it, and transfer project data separately. Share only the public account ID with another person. Vehicle access is explicit per project. Password changes on one device do not change old identity backups or other devices.

Transfer & backup exports the full project and attachments. Import previews the changes and replaces the receiving project after review. Export both copies before resolving divergent edits. Local encrypted pairing and supported shared-folder sync reuse the project history and conflict checks. Use matching app versions on connected devices. Actual radio connectivity still depends on hardware and system permissions.

## Software updates and public downloads

The app checks the fixed public repository **Modzwastaken/l4ntrak-downloads** without an access code, token or settings file. A published feed and its installer files are required. Public installers and the update feed are published in the downloads repository. The feed and every downloaded installer segment are hash-checked before installation.

The owner can prepare the publication directory with `python3 tools/prepare_public_release.py --packages <release-folder> --out <publication-folder>`. Its PUBLISHING.md describes the remaining owner publication step. Preparing the directory does not publish it. Verify the manifest and an installer while signed out before announcing public availability.

The update manager uses only the public feed. No token-entry form is present, no token is required from app users, and legacy saved updater credentials are removed.

Verified downloads check segment and complete-package hashes, size, version and package identity. Android also checks signing identity before installer handoff. Updates remain user initiated and require system installation approval. Opening the installer does not prove installation completed.

## Verification

See RELEASE_3.4.2.md, FEATURE_AND_TEST_REPORT.md and VALIDATION_3.4.2.json for recorded results and limitations. Automated fixtures exercise UI, backend data, simulated GPS/routes/audio/media and native compilation/stub behavior. They do not replace physical Android/GTK installation, moving GPS, Bluetooth, audible camera chimes, microphone recognition, notification access, live publisher availability or on-device inference timing checks.

## 3.4.4 patch

See RELEASE_3.4.4.md. Settings → Sync Now requests the paired phone to check both copies, even with phone Auto Sync off. Keep both apps open on the same local connection. For live GPS, select the same vehicle and open Maps on both devices; stationary fixes work. Save nearby settings in Maps to retain the choice across restarts. Sharing runs only in foreground Maps. Prefer paired PC AI now falls back to the saved phone model; Phone only does not need a PC connection. General answers need an installed model; music and sync controls do not.

## 3.5.0 connected update

- Original-inspired icon: white sedan, cyan road lines and amber navigation pointer on navy.
- Live hub music controller detects an active Android media session, Linux MPRIS player or local Maps queue. Control this device or a fresh paired device on your own account. Remote controls require saved permission on the receiving device, expire after 15 seconds and show acknowledgement.
- Paired devices exchange short-lived media status during foreground heartbeats. Vehicle edits/files retain verified snapshot sync and conflict review; this is not simultaneous collaborative editing.
- More prominent two-note camera warning and amber Camera Ahead banner. Existing GPS checks, entry deduplication and 15-second cooldown remain. Android uses media volume; no forced volume change.
- Audio-only direct and group voice calls for up to six members, with encrypted/signed friend signaling, explicit microphone permission, mute/deafen and foreground cleanup. Requires a working local/private-VPN WebRTC path. No hosted TURN relay, background calls or recording.
- Friends delivery receipts and configurable private VPN peer addresses. Existing identities and histories stay local to each device; vehicle sync does not silently transfer friend private keys.
- Private VPN IPv4 pairing support, including Tailscale's 100.64.0.0/10 range. Remote PC guide in Live hub; keep both apps open and allow the documented ports between your own devices.
- Linux native installation dialog verifies the downloaded DEB again, invokes system authorization, shows output and confirms installed version. Requires pkexec and gdebi. Cancel/error states stay visible. Save DEB and terminal fallback remain available.
- Delete unwanted visual parts from their editor without deleting the linked build job or model file.
- Six-step quick setup or ten-step guided setup, account-scoped recoverable drafts and corrected location/update/nearby guidance. Device page-focus presets and optional quiet interface sounds.

Install over the existing app; do not uninstall. Update both devices for the hub protocol. A PC still running 3.4.4 may need this DEB installed manually once before the new native installation bridge is available.

Physical Android/GTK permissions, actual system upgrade, road GPS/audio, Bluetooth and off-network VPN behavior still require your device testing. Synthetic browser audio is not a road or hardware audio test.

## Free app, optional accessories

All L4NTrak app features are free to use with no subscription gates. Compatible optional paid accessories remain supported, including Bluetooth audio and Meshtastic hardware where available. Hardware, connectivity and third-party provider charges are separate. No third-party paid entitlement is bypassed.

## Chat-only VPN connection

Friends → Connection settings is separate from Home-PC pairing. Both friends install/connect their private VPN, exchange public friend cards, and add each other's VPN IPv4 address. Enable VPN only to disable LAN chat broadcasts, then Save connection and Connect chat & calls on both apps. Allow UDP 47773 between these VPN peers. This does not grant vehicle, files, GPS, AI or music access. Keep both apps open; there is no offline messaging server.

VPN-only voice removes LAN candidates and requires a usable VPN interface. Optional My VPN IPv4 supports private overlays beyond Tailscale. Your VPN provider and VPN peers can see VPN addressing; this is not anonymity from the VPN service. Local identities/history rely on your device storage protection.
