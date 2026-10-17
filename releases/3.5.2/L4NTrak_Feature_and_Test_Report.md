# L4NTrak 3.5.2 — built-in WireGuard and music/nearby fixes

Install over the existing app on PC and phone. Do not uninstall or clear app data.

## Built-in private VPN

Live hub → Connection setup → Built-in private VPN now contains native WireGuard controls. Android includes the official WireGuard tunnel library (1.0.20260102); Linux uses the system WireGuard tools installed with the DEB. No separate VPN client app is required. Device-local private keys stay in native private files; only public peer cards enter the shared interface. Profiles are separate per account and per device.

1. On each device, open Device setup & public peer card. The app assigns a 10.77.x.x address. Choose unique addresses.
2. At least one device needs a reachable endpoint. For a home PC, enter its reachable hostname/public address and UDP listen port (normally 51820), then forward/allow that UDP port on its router/firewall. The endpoint in a shared peer card can reveal that host's public address. Carrier-grade NAT may require a reachable server.
3. Save setup, exchange public peer cards privately, and add each device's card on the other device. Save again. Never add your own card as a peer.
4. Connect on both devices and approve Android VPN consent / Linux system authorization. A started interface is not proof of remote reachability. Android reports recent verified WireGuard handshakes when available.
5. For your own PC/phone, use the peer's 10.77.x.x address in normal Device pairing and use the private pairing code. For friends, choose Use these VPN peers for Friends, then exchange friend IDs separately. VPN peers do not receive vehicle, file, AI or music-control permissions.

Only selected peer host routes in 10.77.0.0/16 use this tunnel. Android additionally limits it to L4NTrak. This is a direct-peer VPN: no automatic NAT traversal, transit relay, router changes, DNS change or whole-internet tunnel. Phone-to-phone links still need a reachable endpoint; this does not turn an unreachable home PC into a public relay. Existing VPNs remain supported. Android asks before replacing another active VPN. Disconnect before switching accounts; Linux tunnel interfaces may persist until explicitly disconnected. Android closes its tunnel when the activity is destroyed. There is no automatic boot connection.

## Included music, maps and interface fixes

- Live hub reads active external music before a paused Maps queue. Paired-phone metadata can appear without remote-control consent; control buttons remain permission-gated.
- Android music detection distinguishes missing notification access, a disconnected listener and missing player metadata. It rebinds the listener, accepts display-title metadata and refreshes on resume or Refresh playback.
- Same-account devices ignore each other in Nearby drivers using rotating private-key-derived aliases, without broadcasting account IDs. Unlabelled older senders are hidden: update participating phones too.
- PCs with phone/IP location remain receive-only. A laptop can share its own fresh local gpsd GPS above 2 mph with accuracy within 30 m. Nearby/friend map packets still omit speed.
- Music and device status stay visible. Connection setup and customization are expandable; Maps drawing tools start collapsed. Explore has a separate Devices & chat category.
- All AI paths have matching current app capability descriptions, including supported navigation, music and VPN setup. This updates app context, not model training data.

All features remain free. Signing identity and existing data are retained. VALIDATION_3.5.2.json records automated coverage. Physical Android VPN consent, native OS interface setup, router reachability, off-network WireGuard handshakes, real media apps, GPS receivers and installation still require device testing. The privileged Linux helper is tested for config validation; no root network interface was created in this build environment.
