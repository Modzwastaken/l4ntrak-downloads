# Owner publication step

Create the public repository Modzwastaken/l4ntrak-downloads with default branch main.
Commit this prepared directory to that repository. Retain releases/latest.json and
all listed .part files; the app verifies every part and the complete installer.
The full APK and DEB are also included for direct downloads from GitHub.
The included workflow verifies every segment, assembles the installers, and publishes
a GitHub Release after a main-branch feed commit. Check the Actions result and Release. Verify releases/latest.json and an installer in a
signed-out browser before announcing availability.

Only the owner publishing the app needs GitHub sign-in. People using L4NTrak do not.
This folder is a prepared publication payload; preparing it does not publish it.
