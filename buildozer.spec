[app]

# (str) Title of your application
title = 视频解析下载

# (str) Package name
package.name = videoparser

# (str) Package domain (important for Android/IOS packages)
package.domain = org.user

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) The version of the app
version = 1.0.0

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy,requests,yt-dlp,mutagen,websockets,pycryptodomex

# (str) Supported orientation (landscape, sensorLandscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,ACCESS_NETWORK_STATE

# (int) Target Android API (should be between API level 16 and 30)
android.api = 30

# (int) Minimum API your APK will support
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 23b

# (bool) If True, then skip trying to update the Android sdk
android.skip_update = False

# (bool) If True, then accept all licenses
android.accept_sdk_license = True

# (str) Android entry point (default is ok)
android.app_entry = main.py

# (str) Android activity (default is ok)
android.activity = org.kivy.android.PythonActivity

# (list) Android services to include
# android.services = 

# (str) The Android command to use for launching the app
# android.launch_activity = 

# (bool) If True, then the application will be built as a service
# android.is_service = False

# (str) The format used to package the app for release mode (aab or apk)
android.release_artifact = apk

# (str) The format used to package the app for debug mode (apk or aab)
android.debug_artifact = apk

# (str) The directory containing the Android SDK
# android.sdk_path = 

# (str) The directory containing the Android NDK
# android.ndk_path = 

# (str) The directory containing the Android Build Tools
# android.build_tools_path = 

# (str) The directory containing the Java JDK
# java.home = 

# (str) Path to the Python interpreter
# python.path = 

# (str) The directory where the build will happen
build_dir = .buildozer

# (str) The directory where the APK will be stored
bin_dir = bin

# (bool) Whether to use the Android SDK emulator
# p4a.android_sdk.auto = True

# (str) Filename of the application (with .apk extension)
# android.app = 

# (list) Patterns to whitelist for inclusion in the APK
# android.whitelist = 

# (list) Patterns to blacklist from inclusion in the APK
# android.blacklist = 

# (str) Path to a custom keystore file for signing the APK
# android.keystore = 

# (str) Alias for the key in the keystore
# android.keyalias = 

# (str) Path to the keystore password file
# android.keystorepw = 

# (str) Path to the key password file
# android.keypw = 

# (str) Path to the Android manifest template
# android.manifest = 

# (str) Path to the Android build.gradle template
# android.gradle = 

# (str) Path to the Android proguard config
# android.proguard = 

# (str) Path to the Android lint config
# android.lint = 

# (str) Path to the Android signing config
# android.signing = 

# (str) Path to the Android application resources
# android.res = 

# (str) Path to the Android assets
# android.assets = 

# (str) Path to the Android native libraries
# android.native_libs = 

# (str) Path to the Android public key for verification
# android.public_key = 

# (str) Path to the Android private key for verification
# android.private_key = 

# (str) Path to the Android certificate
# android.certificate = 

# (str) Path to the Android key
# android.key = 

# (str) Path to the Android password
# android.password = 

# (str) Path to the Android alias
# android.alias = 

# (str) Path to the Android store password
# android.storepass = 

# (str) Path to the Android key password
# android.keypass = 

# (str) Path to the Android keystore type
# android.keystoretype = 

# (str) Path to the Android key algorithm
# android.keyalg = 

# (str) Path to the Android key size
# android.keysize = 

# (str) Path to the Android signature algorithm
# android.sigalg = 

# (str) Path to the Android digest algorithm
# android.digestalg = 

# (str) Path to the Android encryption algorithm
# android.encalg = 

# (str) Path to the Android padding scheme
# android.padding = 

# (str) Path to the Android mode
# android.mode = 

# (str) Path to the Android provider
# android.provider = 

# (str) Path to the Android algorithm
# android.algorithm = 

# (str) Path to the Android salt
# android.salt = 

# (str) Path to the Android iteration count
# android.iterationcount = 

# (str) Path to the Android key length
# android.keylength = 

# (str) Path to the Android IV
# android.iv = 

# (str) Path to the Android AAD
# android.aad = 

# (str) Path to the Android tag length
# android.taglength = 

# (str) Path to the Android Mac length
# android.maclength = 

# (str) Path to the Android nonce
# android.nonce = 

# (str) Path to the Android associated data
# android.associateddata = 

# (str) Path to the Android counter
# android.counter = 

# (str) Path to the Android initial counter value
# android.initialcountervalue = 

# (str) Path to the Android re-key limit
# android.rekeylimit = 

# (str) Path to the Android re-key interval
# android.rekeyinterval = 

# (str) Path to the Android re-key mode
# android.rekeymode = 

# (str) Path to the Android re-key algorithm
# android.rekeyalgorithm = 

# (str) Path to the Android re-key salt
# android.rekeysalt = 

# (str) Path to the Android re-key iteration count
# android.rekeyiterationcount = 

# (str) Path to the Android re-key key length
# android.rekeykeylength = 

# (str) Path to the Android re-key IV
# android.rekeyiv = 

# (str) Path to the Android re-key AAD
# android.rekeyaad = 

# (str) Path to the Android re-key tag length
# android.rekeytaglength = 

# (str) Path to the Android re-key Mac length
# android.rekeymaclength = 

# (str) Path to the Android re-key nonce
# android.rekeynonce = 

# (str) Path to the Android re-key associated data
# android.rekeyassociateddata = 

# (str) Path to the Android re-key counter
# android.rekeycounter = 

# (str) Path to the Android re-key initial counter value
# android.rekeyinitialcountervalue = 

# (str) Path to the Android re-key re-key limit
# android.rekeyrekeylimit = 

# (str) Path to the Android re-key re-key interval
# android.rekeyrekeyinterval = 

# (str) Path to the Android re-key re-key mode
# android.rekeyrekeymode = 

# (str) Path to the Android re-key re-key algorithm
# android.rekeyrekeyalgorithm = 

# (str) Path to the Android re-key re-key salt
# android.rekeyrekeysalt = 

# (str) Path to the Android re-key re-key iteration count
# android.rekeyrekeyiterationcount = 

# (str) Path to the Android re-key re-key key length
# android.rekeyrekeykeylength = 

# (str) Path to the Android re-key re-key IV
# android.rekeyrekeyiv = 

# (str) Path to the Android re-key re-key AAD
# android.rekeyrekeyaad = 

# (str) Path to the Android re-key re-key tag length
# android.rekeyrekeytaglength = 

# (str) Path to the Android re-key re-key Mac length
# android.rekeyrekeymaclength = 

# (str) Path to the Android re-key re-key nonce
# android.rekeyrekeynonce = 

# (str) Path to the Android re-key re-key associated data
# android.rekeyrekeyassociateddata = 

# (str) Path to the Android re-key re-key counter
# android.rekeyrekeycounter = 

# (str) Path to the Android re-key re-key initial counter value
# android.rekeyrekeyinitialcountervalue = 
