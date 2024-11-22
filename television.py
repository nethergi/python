class Television():
    '''Class dedicated to TV functions'''
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        '''TV object is created with preinitialized variables of:
            status = False (off)
            muted = False (not muted)
            channel = Gobal minimum channel (default: 0)
            volume = Gobal minimum volume (default: 0)'''
        self.status = False
        self.muted = False
        self.channel = Television.MIN_CHANNEL
        self.volume = Television.MIN_VOLUME

    def power(self):
        '''Toggles power'''
        if self.status:
            self.status = False
        else:
            self.status = True

    def mute(self):
        '''Toggles mute'''
        if self.muted:
            self.muted = False
        else:
            self.muted = True

    def channel_up(self):
        '''Increments channel, wraps at global max'''
        if self.channel < Television.MAX_CHANNEL:
            self.channel += 1
        else:
            self.channel = Television.MIN_CHANNEL
    
    def channel_down(self):
        '''Decrements channel, wraps at global min'''
        if self.channel > Television.MIN_CHANNEL:
            self.channel -= 1
        else:
            self.channel = Television.MAX_CHANNEL

    def volume_up(self):
        '''Increments volume, wraps at global max'''
        if self.volume < Television.MAX_VOLUME:
            self.volume += 1
        else:
            self.volume = Television.MIN_VOLUME

    def volume_down(self):
        '''Decrements volume, wraps at global min'''
        if self.volume > Television.MIN_VOLUME:
            self.volume -= 1
        else:
            self.volume = Television.MAX_VOLUME

    def __str__(self) -> str:
        '''ToString returns "Power - [status], Channel - [channel], Volume - [volume]"'''
        return f"Power - {self.status}, Channel - {self.channel}, Volume - {self.volume}"
