# SoundBoard.py
The script will use the GPIO ports on a Raspberry Pi Model 4 to trigger sounds.
The sounds are MP3 files stored in the Sounds folder and will be played using the `playsound` library.
Each GPIO port will correspond to a specific sound. A list of all available GPIO ports: 5, 6, 7, 12, 13, 19, 20, 21, 26.
The mapping between GPIO ports and sounds will be stored in a configuration object (a Python dictionary).
The script will use analog signals created by pushing a button connected to the GPIO port to trigger the sounds.
If a button is pressed before the current sound is done, the current sound will be stopped and the new one will start.
The script will have a reasonable amount of documentation.
The script will output messages to the console for GPIO input, sounds that are played, and error messages.
If a button is pressed while a sound is already playing, the current sound will be stopped and the new one will start
If a button is pressed that is not mapped to any sound, an error message will be output to the console.
If the script is interrupted while a sound is playing, the sound will stop.
The script will listen for an interrupt signal (Ctrl+C) and stop the currently playing sound.
The script will also handle errors, such as when a button is pressed that is not mapped to any sound, and output an error message to the console.

Here is an example of what the configuration object might look like:
sound_mapping = {
  5: 'sound1.mp3',
  6: 'sound2.mp3',
}