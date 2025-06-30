[app]
title = Voice Command Sender
package.name = voicecommand
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy,requests,pyjnius
orientation = portrait
fullscreen = 0
android.permissions = RECORD_AUDIO,INTERNET
android.api = 31
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a,armeabi-v7a
android.gradle_dependencies = 'androidx.appcompat:appcompat:1.2.0'
