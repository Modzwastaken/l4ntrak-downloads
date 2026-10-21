# L4NTrak 3.6.0

[Get Android, Windows and Linux downloads](https://github.com/Modzwastaken/l4ntrak-downloads/releases/latest). The app’s **Software updates** page also includes all three downloads. Updates are free; optional hardware, network services and mobile data may have their own costs.

## Install or update

- **Android ARM64:** install the APK over the existing app. Keep the same app and signing identity; do not uninstall or clear app data. Approve Android’s installation prompt.
- **Linux Mint/Debian:** open the DEB with your package installer. It upgrades `lancer-garage` and retains its data. Package dependencies include GTK/WebKit, Python, media and WireGuard tools.
- **Windows 10/11 x64 portable edition:** extract the entire ZIP, then double-click **Start L4NTrak.cmd**. The interface opens in your default browser. The local host stays running until you choose **Quit**. No separate Python installation is needed. Records live in `%LOCALAPPDATA%\L4NTrak`. To upgrade, quit the old host, extract the new ZIP into a new folder, then launch it. Keep your data directory.

Export a full account ZIP or project backup before a major update. Android/Linux upgrades keep their existing data locations. Review the OS installer’s result and reopen the app to confirm the installed version.

Setup revision 4 offers seven quick steps or a guided tour. Existing vehicle data is retained. Sign in with your existing account; import its identity or full account ZIP on another device to keep the same account.

## Maps and Trak

Open **Maps → Locate me**, grant location permission and wait for an accurate fix. Search for an address or a saved place, choose the matching result, get a route and start guidance. Road directions come from OSRM/OpenStreetMap, with no live traffic. Cached directions and imported offline map packs have separate controls. Keep Maps in the foreground for location and guidance.

In Map options, **Guidance preferences** contains:

| Control | Behavior |
| --- | --- |
| Time advance: Early | Announces advance cues farther ahead, using current speed |
| Time advance: Normal | Standard advance timing |
| Time advance: Late | Announces advance cues closer to the turn |
| Normal assistant | Full road instructions |
| Rally assistant | Concise road calls with a next-turn preview |
| Race assistant | Short calls for closed-course planning |

The final turn cue retains its GPS accuracy guard. Modes do not invent corner grades, racing lines, braking points, road access or lap times. Timing and mode are saved with the vehicle and included in normal project sync.

Try **“set a route to Home”**, **“add a stop at Fuel”**, **“start navigation”**, **“next turn”**, **“set time advance to early”**, **“use rally mode”**, **“open music”**, **“next track”** or **“sync now”**. These supported actions run without model inference. Ambiguous addresses require you to select a match.

## Hey Trak and voice

**Ask by voice** listens for one question. You can include “Hey Trak” or ask directly.

For wake listening, open **Maps → Trak voice** and enable **Listen for “Hey Trak” while Maps is visible**. Say the wake phrase and question together, or pause briefly after “Hey Trak”. Recognition reopens after silence or an answer until stopped. Android may play its recognition tone on each restart. Microphone permission is required. On-device recognition is preferred; system/browser recognition may use a provider and requires explicit consent.

Listening stops when you disable it, leave Maps, background the app, sign out or enter Quiet Trak. Returning to the app does not silently restart the microphone. Permission or speech-service errors require your attention rather than an automatic retry loop. Linux can install optional offline Vosk recognition; Windows and hosted browsers use supported browser speech recognition. Browser support and road noise affect results. Typed commands remain available.

## Friends, chat and calls

1. **Connect:** use the same Wi-Fi/hotspot or a working private VPN. Enable Connect chat & calls on both devices and keep both apps open.
2. **Add each other:** share your public friend card privately, paste your friend’s card, and have them add yours. Verify their identity through a trusted channel. The mobile Share button uses your device’s share sheet.
3. **Choose a conversation:** send a message or tap **Call**. The other person accepts; microphone access is requested then. “Delivered” confirms receipt by their app.

Groups, profile changes and network configuration are under **Advanced**. Calls support up to six participants over a usable local/VPN WebRTC path. There is no hosted relay, offline delivery queue or recording. Messages are signed and encrypted in transit; history and friend identity keys use this device’s storage protection. Friend cards do not grant vehicle or device-control access. Friend identities/history are device-local, separate from vehicle Trak chats.

## Music and your devices

**Live hub** detects the active music session. On Android, allow song information in Notification access, start a song in your music app, return and tap **Refresh playback**. Reading song information and allowing remote controls are separate choices. Linux uses MPRIS-compatible players. Windows provides toggle/next/previous/volume media keys; this portable edition does not read Windows track metadata. Maps can also use its local music queue.

Pair your own phone and PC under **Live hub → Pair devices**. Grant access only to the vehicles and actions you intend to share. Sync includes saved records, settings, directions, Trak chats, photos, receipts and supported attachments. Independent edits pause for conflict review. **Model & sync check** compares saved sections and actual file hashes. An account sign-in alone is not a cloud sync service. Device permissions, VPN private keys, friend chat identity/history, runtime binaries, offline map packs and downloaded AI model weights stay device-local.

Fast, concise AI replies are the default. Smaller installed models suit phones; choose the paired PC for heavier inference. Model weights download separately. Windows uses the official [Ollama Windows installation](https://ollama.com/download/windows); Linux can use the managed installer. App capability updates do not update a model’s training knowledge. Current facts need current research sources.

## Apple and other browser clients

On the PC, open **Live hub → Browser access**, start hosting and create an invitation. Open one of the displayed HTTPS addresses on the other device and enter its one-use code within five minutes. Hosting is off until started; no router ports are opened automatically. The PC must stay running. If asked, allow TCP 47774 on a trusted private network.

The host uses a device-local HTTPS certificate. For GPS and microphone support, install and trust that certificate after comparing its SHA-256 fingerprint privately with the PC. The certificate is available at `/certificate.cer` on the displayed host address. On iOS/iPadOS, install the downloaded certificate profile, then enable full trust in **Settings → General → About → Certificate Trust Settings**. Server certificates renew locally when addresses change; the trusted device root stays the same. If the root certificate itself changes, verify and trust the new root again.

Browser clients use their own GPS after **Locate me** and permission. **Share my GPS with this PC** is a separate, optional foreground choice. Route progress and speech output run on the browser. Browser edits save directly into the PC’s current vehicle, so there is no second database to synchronize. Browser access ends on PC sign-out, account/session changes, vehicle changes, stopping hosting, or session expiry. Use Disconnect browser to end your own session. Account keys, OS actions, native friend transport, VPN activation, pairing and installation stay on the PC. Safari background tracking, speech recognition, notification access and cross-app music control differ from native Android.

## Nearby and private connections

Nearby sharing is optional. Your other devices on the same imported account are suppressed as nearby users. A PC can share only its own fresh GPS, with accuracy within 30 m and speed above 2 mph; phone-relayed, browser-relayed and IP positions cannot make a stationary PC appear as another driver. An optional local gpsd receiver can provide a laptop’s own GPS.

Same-network encrypted pairing and friends transport need no separate VPN app. Across networks, built-in WireGuard on Android/Linux uses native private keys and selected `10.77.x.x` peer routes. Open **Live hub → Connection setup → Built-in private VPN**, exchange public peer cards, save both devices and connect. At least one endpoint must be reachable, often through router UDP forwarding. There is no automatic NAT traversal or transit relay. Android VPN consent and Linux authorization remain required. Windows can use an existing private VPN interface; built-in activation and native Bluetooth are not supplied in this edition. VPN connectivity never grants pairing or friend permissions automatically.

## Updates and troubleshooting

After sign-in, a quiet banner alerts you to new releases. Dismiss a version or review it in Software updates. Downloads are checked against the public release feed and SHA-256; installation remains your choice. All-device direct downloads and release checksums are on the same page. No GitHub access token is needed.

If music is missing, check Notification access and Refresh playback. If voice fails, check microphone and speech-provider permissions. If the browser loses access, sign in on the PC and create another invitation. For sync differences, run Model & sync check before resolving a conflict. App health provides limited, logged layout repairs; it does not replace software updates or restore deleted data.

See `DEVELOPER.md`, `RELEASE_3.6.0.md` and `FEATURE_AND_TEST_REPORT.md` for development and validation details.
