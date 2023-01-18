# Minecraft-SFX-Scraper

The purpose of this program is to extract all of the .ogg sound files from Minecraft's data folder. 
This has currently only been tested with Java edition 1.19.2. It will likely work with other versions of Java edition, but I am completely unsure about Bedrock.

TO MAKE IT WORK, YOU WILL NEED:

-The scraper.py file from this repo
-The [Version].json file from .minecraft/assets/indexes -- use the most recent, in my case it was 1.19.json
-The entire objects folder from .minecraft/assets


Your file directory should look like this:

  scraper.py
  
  [Version].json
  
  objects/
  
  

Once this is setup, run the program and it will create a new directory in the root folder of this project called "sounds" containing numerous folders containing all the audio files you were looking for.

Hope this is helpful!
