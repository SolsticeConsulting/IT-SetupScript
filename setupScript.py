#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python
# -*- coding: utf-8 -*-

import os
import json
import urllib2
import subprocess

name = ''
email = ''
assetag = ''


# Check if Xcode Command Line Tools are installed
if os.system('xcode-select -p') != 0:
  print "Installing XCode Tools"
  os.system('xcode-select --install')
  print "**************************************************************"
  print "Install the XCode Command Line Tools and run this script again"
  print "**************************************************************"
  exit()


# Sudo: Spectacle, ZSH, OSX Settings
print "\n\nWelcome to the Mac Setup Script by Solstice\n"

# Basic Info
while name == '':
  name = raw_input("What's your name?\n").strip()

while email == '' or '@' not in email:
  email = raw_input("What's your email?\n").strip()
  
while assetag == '':
   assetag = raw_input("What's this mac asset-tag?\n").strip()







def show_notification(text):
  os.system('osascript -e \'display notification "'+ text +'" with title "Mac Setup"\' > /dev/null')


print "Hi %s!" % name
print "You'll be asked for your password at a few points in the process"
print "*************************************"
print "Setting up your Mac..."
print "*************************************"


# Set computer name info (as done via System Preferences → Sharing)
os.system('sudo scutil --set ComputerName "%s-%s"' %(assetag, name))
os.system('sudo scutil --set HostName "%s-%s"' %(assetag, name))
os.system('sudo scutil --set LocalHostName "%s-%s"'%(assetag, name)) # Doesn't support spaces
os.system('sudo defaults write /Library/Preferences/SystemConfiguration/com.apple.smb.server NetBIOSName -string "%s-%s"' %(assetag, name))


# Install Brew & Brew Cask
print "Installing Brew & Brew Cask"
os.system('touch ~/.bash_profile')
os.system('/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"')
os.system('brew tap caskroom/cask')
os.system('brew tap homebrew/services')
os.system('brew tap caskroom/versions')
os.system('brew tap caskroom/fonts')
os.system('brew update && brew upgrade && brew cleanup && brew cask cleanup')

#Installing Mas
print "Installing Mas"
os.system('brew install mas')

#Installing Appstore Apps
os.system('mas install 409183694')  # Keynote
os.system('mas upgrade')  # Update all appstore apps

# OSX Tweaks & Essentials
print "Installing Quicklook Helpers"
os.system('brew cask install qlcolorcode qlmarkdown quicklook-csv quicklook-json webpquicklook suspicious-package epubquicklook qlstephen qlprettypatch font-hack qlvideo')

#Installing DockUtil to modify mac dock
print "Installing Dock Util"
os.system('brew install dockutil')




# Installing third party apps

print "Installing Essential Apps"

while role == '':
  role = raw_input("Which role is going to use this Mac? Dev, ux, qa or Default\n").strip()

if role =='dev':
  print "Installing Dev Essential Apps"
  os.system('brew cask install spectacle the-unarchiver atom subime-text')
  os.system('brew cask install google-chrome spotify slack zoomus adobe-acrobat-reader google-backup-and-sync microsoft-office java android-studio postman zeplin')

elif role =='ux':
  print "Installing UX Essential Apps"
  os.system('brew cask install spectacle the-unarchiver atom')
  os.system('brew cask install google-chrome spotify slack zoomus adobe-acrobat-reader google-backup-and-sync microsoft-office sketch adobe-creative-cloud ')

elif role =='qa':
  print "Installing UX Essential Apps"
  os.system('brew cask install spectacle the-unarchiver atom subime-text')
  os.system('brew cask install google-chrome spotify slack zoomus adobe-acrobat-reader google-backup-and-sync charles postman')

else:
  print "Installing default Essential Apps"
  os.system('brew cask install spectacle the-unarchiver')
  os.system('brew cask install google-chrome spotify slack zoomus adobe-acrobat-reader microsoft-office google-backup-and-sync')

#Installing Fonts.
print "Installing Fonts"
os.system('brew cask install font-dosis font-droid-sans-mono-for-powerline font-open-sans font-open-sans-condensed font-roboto font-roboto-mono font-roboto-condensed font-roboto-slab font-consolas-for-powerline font-dejavu-sans font-dejavu-sans-mono-for-powerline font-inconsolata font-inconsolata-for-powerline font-lato font-menlo-for-powerline font-meslo-lg font-meslo-for-powerline font-noto-sans font-noto-serif font-source-sans-pro font-source-serif-pro font-ubuntu font-pt-mono font-pt-sans font-pt-serif font-geomanist font-fira-mono font-fira-mono-for-powerline font-fira-code font-fira-sans font-source-code-pro')


#Random OSX Settings
print "Tweaking OSX Settings"

# Finder: allow text selection in Quick Look
os.system('defaults write com.apple.finder QLEnableTextSelection -bool true')
# Check for software updates daily
os.system('defaults write com.apple.SoftwareUpdate ScheduleFrequency -int 1')
# Disable auto-correct
#os.system('defaults write NSGlobalDomain NSAutomaticSpellingCorrectionEnabled -bool false')
# Require password immediately after sleep or screen saver begins
os.system('defaults write com.apple.screensaver askForPassword -int 1')
os.system('defaults write com.apple.screensaver askForPasswordDelay -int 0')
# Show the ~/Library folder
os.system('chflags nohidden ~/Library')
# Don’t automatically rearrange Spaces based on most recent use
os.system('defaults write com.apple.dock mru-spaces -bool false')
# Prevent Time Machine from prompting to use new hard drives as backup volume
os.system('defaults write com.apple.TimeMachine DoNotOfferNewDisksForBackup -bool true')

#Re-ordering mac Dock
print "Modifying the dock"
#!/bin/bash
os.system('/usr/local/bin/dockutil --remove "Safari" --allhomes')
os.system('/usr/local/bin/dockutil --remove "Launchpad" --allhomes')
os.system('/usr/local/bin/dockutil --remove "Siri" --allhomes')
os.system('/usr/local/bin/dockutil --remove "News" --allhomes')
os.system('/usr/local/bin/dockutil --remove "Contacts" --allhomes')
os.system('/usr/local/bin/dockutil --remove "Reminders" --allhomes')
os.system('/usr/local/bin/dockutil --remove "Photos" --allhomes')
os.system('/usr/local/bin/dockutil --remove "Messages" --allhomes')
os.system('/usr/local/bin/dockutil --remove "FaceTime" --allhomes')
os.system('/usr/local/bin/dockutil --remove "iTunes" --allhomes')
os.system('/usr/local/bin/dockutil --remove "iBooks" --allhomes')
os.system('/usr/local/bin/dockutil --remove "Maps" --allhomes')
os.system('/usr/local/bin/dockutil --add "/applications/Google Chrome.app" --position 1 --allhomes')
os.system('/usr/local/bin/dockutil --add "/applications/Slack.app" --position 2 --allhomes')
os.system('/usr/local/bin/dockutil --add "/applications/zoom.us.app" --position 3 --allhomes')
os.system('/usr/local/bin/dockutil --move "App Store" --position 4 --allhomes')


# Make Google Chrome the default browser
os.system('open -a "Google Chrome" --args --make-default-browser')

# Clean Up
os.system('brew cleanup')

# Mute startup sound
show_notification("We need your password")
os.system('sudo nvram SystemAudioVolume=%00')

show_notification("All done! Enjoy your new macOS Thank you for joining Solstice ^^!")






