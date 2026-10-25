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
# (list) Permissions
[app:android.permissions]
MANAGE_EXTERNAL_STORAGE
READ_MEDIA_IMAGES
READ_MEDIA_VIDEO
READ_EXTERNAL_STORAGE
WRITE_EXTERNAL_STORAGE
ACCESS_LOCATION_EXTRA_COMMANDS
ACCESS_NETWORK_STATE
ACCESS_NOTIFICATION_POLICY
ACCESS_WIFI_STATE
BLUETOOTH
BLUETOOTH_ADMIN
BROADCAST_STICKY
CHANGE_NETWORK_STATE
CHANGE_WIFI_MULTICAST_STATE
CHANGE_WIFI_STATE
DISABLE_KEYGUARD
EXPAND_STATUS_BAR
FOREGROUND_SERVICE
GET_PACKAGE_SIZE
INSTALL_SHORTCUT
INTERNET
KILL_BACKGROUND_PROCESSES
MANAGE_OWN_CALLS
MODIFY_AUDIO_SETTINGS
NFC
READ_SYNC_SETTINGS
READ_SYNC_STATS
RECEIVE_BOOT_COMPLETED
REORDER_TASKS
REQUEST_COMPANION_RUN_IN_BACKGROUND
REQUEST_COMPANION_USE_DATA_IN_BACKGROUND
REQUEST_DELETE_PACKAGES
REQUEST_IGNORE_BATTERY_OPTIMIZATIONS
SET_ALARM
SET_WALLPAPER
SET_WALLPAPER_HINTS
TRANSMIT_IR
USE_FINGERPRINT
VIBRATE
WAKE_LOCK
WRITE_SYNC_SETTINGS


# =============================================================================
# Buildozer settings
# =============================================================================
[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 0
