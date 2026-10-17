# L4NTrak 3.5.0

Install over the existing Android and Linux apps. Both devices need this update for Live hub.

## New behavior

- Original-inspired icon: white sedan, cyan road lines and amber navigation pointer on navy.
- Live hub music controller detects an active Android media session, Linux MPRIS player or local Maps queue. Control this device or a fresh paired device on your own account. Remote controls require saved permission on the receiving device, expire after 15 seconds and show acknowledgement.
- Paired devices exchange short-lived media status during foreground heartbeats. Vehicle edits/files retain verified snapshot sync and conflict review; this is not simultaneous collaborative editing.
- Assistant navigation commands now open Maps and set a verified road route for a unique saved place, coordinate or search result. Multiple matches stay a visible choice. Add stops, start guidance, next turn/ETA, reroute and map controls work without model inference. Saved-vehicle questions receive a real record lookup before inference; tool logs show what was read.
- More prominent two-note camera warning and amber Camera Ahead banner. Existing GPS checks, entry deduplication and 15-second cooldown remain. Android uses media volume; no forced volume change.
- Audio-only direct and group voice calls for up to six members, with encrypted/signed friend signaling, explicit microphone permission, mute/deafen and foreground cleanup. Requires a working local/private-VPN WebRTC path. No hosted TURN relay, background calls or recording.
- Friends delivery receipts and a separate chat-only VPN connection. VPN-only mode sends to configured peers without LAN broadcast and rejects other transport senders; friend identities and signed encryption still authenticate every message. Voice signaling removes LAN/mDNS candidates in VPN-only mode. Chat access does not enable vehicle/device hub features. Existing identities and histories stay local to each device; vehicle sync does not silently transfer friend private keys.
- Private VPN IPv4 pairing support, including Tailscale's 100.64.0.0/10 range. Remote PC guide in Live hub; keep both apps open and allow the documented ports between your own devices.
- Linux native installation dialog verifies the downloaded DEB again, invokes system authorization, shows output and confirms installed version. Requires pkexec and gdebi. Cancel/error states stay visible. Save DEB and terminal fallback remain available.
- Delete unwanted visual parts from their editor without deleting the linked build job or model file.
- Six-step quick setup or ten-step guided setup, account-scoped recoverable drafts and corrected location/update/nearby guidance. Device page-focus presets and optional quiet interface sounds.

Install over the existing app; do not uninstall. Update both devices for the hub protocol. A PC still running 3.4.4 may need this DEB installed manually once before the new native installation bridge is available.

Physical Android/GTK permissions, actual system upgrade, road GPS/audio, Bluetooth and off-network VPN behavior still require your device testing. Synthetic browser audio is not a road or hardware audio test.

All app features remain free with no subscription gate; compatible optional paid accessories remain supported. Hardware and third-party provider charges are separate.

## Validation

The machine-readable VALIDATION_3.5.0.json records results and limitations. Backend tests cover owner/account scoping, consent, targeted command acknowledgement and expiry, VPN address boundaries and installer revalidation. Android is compiled and signed with the existing app key. The DEB is extracted and its server smoke-tested. Browser tests use synthetic media; physical audio, microphone permissions, package-manager authorization and real off-network behavior require device testing.

Existing sync tests cover signed accounts, encrypted transfers, file hashes, stale versions, access revocation and conflicting edits. Friend identities/history remain separate per device; they are not copied through shared vehicle snapshots. Calls remain foreground only and need direct network reachability.
