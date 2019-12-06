#!/usr/bin/env bash
/usr/local/bin/rclone copy "$HOME/Music/iTunes/iTunes Media/Music/" dropbox:MusicBackup/ -u --exclude=.DS_Store
