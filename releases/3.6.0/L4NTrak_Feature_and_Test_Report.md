# L4NTrak 3.6.0 — feature and validation report

3.6.0 adds a Windows x64 portable edition, authenticated HTTPS browser access with device GPS, Early/Normal/Late direction timing, functional Normal/Rally/Race guidance wording, clearer friends/setup screens, quiet update alerts, all-device downloads and restored foreground Hey Trak listening.

## Verified

- Full core run: 120 Python cases, 118 passed and two historical personal-fixture cases skipped; 20 JavaScript suites passed.
- Two additional JavaScript suites passed for timing/action routing and wake-listening lifecycle.
- 26 browser suites passed after adapting legacy expectations to the new setup/Advanced menus and waiting for asynchronous camera installation. Coverage includes accounts, Android bridge, phone/desktop layouts, maps/routing, 3D, updates, verified transfers, sync, music, private chat settings and three-peer WebRTC with simulated microphones.
- Final feature UI checks exercised authenticated update alerts/dismissal; all three platform downloads; clean sign-in including late call callbacks; quick preference changes; HTTPS invitation sign-in; browser GPS sharing to PC; shared settings; browser speech/wake handoff with a controlled recognizer; and revocation.
- Six final real HTTPS gateway tests passed, including a normal trust-verifying TLS client using the exported device root. Account/vehicle scope, one-use invitations, secure cookies, request-origin/CSRF checks and blocked native actions were exercised.
- Windows packaged runtime passed the same six gateway/account/record tests on a Windows Server 2025 GitHub runner: https://github.com/Modzwastaken/l4ntrak/actions/runs/39540859671 . This is native Windows execution, not an emulation claim.
- Android SDK compilation, original-key signing and signature verification passed. The release APK’s web assets match shipping source and retain all four WireGuard native ABI libraries. Windows bundle application bytes and PE executables were checked against source.

## Platform behavior

Windows uses a bundled runtime and default-browser UI; extract the whole ZIP and run Start L4NTrak.cmd. The PC host continues until Quit. Linux uses its GTK/WebKit window. Android retains its native bridge. Hosted Apple browsers save to the PC’s active project and can use their own foreground GPS, route guidance and speech after HTTPS trust/permissions. The root certificate is device-local; server certificates include server-auth purpose and address SANs. Device/account permissions and OS actions remain on the PC.

Time advance changes speed-aware advance cues; the final turn cue retains its accuracy guard. Modes use actual road maneuvers. Rally adds a next-turn preview; Race is concise and does not fabricate corner grades, racing lines or braking points. Preferences are saved and shared with the project.

Hey Trak is opt-in foreground recognition. Wake listening can restart after silence/answers and supports a split wake phrase and question. Tap-to-ask remains a single session. Leaving Maps, backgrounding, account lock, Quiet Trak, or permission/service errors stops listening. Android services may play recognition tones. Browser speech may use its provider only after explicit consent.

## Limits and required device checks

- Two historical personal-fixture Python cases skipped in the 120-case full run (118 passed). The final gateway six-case suite was run separately.
- Browser GPS, speech-recognition events and microphone audio use controlled fixtures; these do not prove physical iPhone/Android GPS or speech quality.
- Three WebRTC peers connected with real browser transport and signed encrypted signaling, using simulated microphones. Real network/NAT, phone delivery and audio quality still need device checks.
- No physical Android, iPhone/iPad, Windows 10/11 desktop, Linux GTK window, Bluetooth hardware or root WireGuard interface was available.
- AI model inference speed was not benchmarked on the user’s hardware. Changes reduce request/context overhead; they do not promise a specific latency.
- Native built-in VPN activation remains Android/Linux only. Windows track metadata and native Bluetooth are not implemented; hosted browsers do not expose native friend transport or cross-app notification/music access.

This report records automated results, not a guarantee of every device, music provider, radio, map provider or network. Test the signed upgrade, real song detection, Hey Trak language pack, GPS, iOS certificate trust and an actual paired-device sync on the target devices. Existing cryptographic pairing, friend membership, VPN route restrictions and same-account nearby suppression remain enforced.
