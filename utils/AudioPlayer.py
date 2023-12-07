from pydub import AudioSegment
from pydub.playback import play
from enum import Enum
from ..soundDict import sounds

enum test = sounds
class Player:
    
    
    def play():
        
        """
        switch signal:
            case Signal_1:
                break
            case Signal_2:
                break 
            case Signale_3:
                break
            case Signal_4:
                break
            case Signal_5:
                break
                """
            
        
        
        song = AudioSegment.from_mp3("Sounds\\ahhhh.mp3" )
        play(song)