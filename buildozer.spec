[app]

# (str) Title of your application
title = Kivy Launcher

# (str) Package name
package.name = launcher

# (str) Package domain (needed for android/ios packaging)
package.domain = org.kivy

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,ttf

# (list) List of directory to exclude
source.exclude_dirs = tests, bin, art

# (str) Application versioning
version = 0.2

# (list) Application requirements
requirements = library,kivy,android

# (str) Supported orientation (one of landscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (str) Source code where the main.py lives (points to your repository root)
source.dir = .

# (list) Source files to include (Leave blank to dynamically package all file paths)
source.include_exts = py,png,jpg,kv,atlas,ttf,txt

# (list) List of directories to exclude (CRUCIAL: Make sure launcher, art, and data are NOT here)
source.exclude_dirs = tests, bin, .buildozer, .git


# =============================================================================
# Android specific
# =============================================================================

# (int) Android API to use
android.api = 33

# (int) Minimum API required
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (str) python-for-android branch to use, defaults to stable
p4a.branch = master

# (str) launchMode to set for the main activity
android.manifest.launch_mode = standard

# (str) The Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.archs = armeabi-v7a, arm64-v8a

# (bool) Automatically accept SDK license
android.accept_sdk_license = True

# =============================================================================
# Permissions
# =============================================================================
[app:android.permissions]
INTERNET
READ_EXTERNAL_STORAGE
WRITE_EXTERNAL_STORAGE
ACCESS_NETWORK_STATE
WAKE_LOCK

# =============================================================================
# Buildozer settings
# =============================================================================
[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 0
