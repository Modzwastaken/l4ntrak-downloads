# L4NTrak 3.5.1 — music detection fixes

Install over the existing app on both devices. Keep app data.

- Live hub checks active device music even when a paused Maps queue exists. Playing external music wins; an actively playing Maps queue remains supported.
- A paired phone playing music can be selected automatically when the PC is idle or paused. Song display does not require remote music-control consent. Remote buttons remain disabled until that device grants control.
- Android shows missing notification access, a disconnected listener or a player with no metadata as separate states. It retries listener binding, accepts display-title metadata and identifies the player. No notification contents are collected or stored.
- Refresh playback and foreground/resume refresh make permission changes and player switching easier to recover. Detection diagnostics travel through the existing account-authenticated hub heartbeat.
- Live hub controls target the detected external player rather than a paused Maps queue. Trak explains music permissions and connection capabilities without model inference. Android, desktop and shared inference paths have matching current app capability descriptions.
- Private connections guidance now clearly exposes the existing built-in encrypted local path over trusted Wi-Fi or a private hotspot, with separate hub and friend permissions. No VPN app is needed on that local path. Separate-network internet connections still require a reachable private VPN. This release does not include a built-in internet VPN or a hosted relay; local mode does not hide local IP addresses from peers.

All features remain free. Existing identities, friends, accounts, vehicle data and signing certificate are retained. Historical migrations and compatibility paths are retained rather than deleted as clutter. This is a focused review of music, AI capability descriptions and connection guidance, not a complete audit of every app screen or an update to local model training data.

Validation and remaining device checks are recorded in VALIDATION_3.5.1.json. Physical Android media players/notification access, audible output, real phone-to-PC delivery and installation still require device testing.
