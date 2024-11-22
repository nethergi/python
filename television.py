class Television():
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        self.status = False
        self.muted = False
        self.channel = Television.MIN_CHANNEL
        self.volume = Television.MIN_VOLUME

    def power(self):
        if self.status:
            self.status = False
        else:
            self.status = True

    def mute(self):
        if self.muted:
            self.muted = False
        else:
            self.muted = True

    def channel_up(self):
        if self.channel < Television.MAX_CHANNEL:
            self.channel += 1
        else:
            self.channel = Television.MIN_CHANNEL
    
    def channel_down(self):
        if self.channel > Television.MIN_CHANNEL:
            self.channel -= 1
        else:
            self.channel = Television.MAX_CHANNEL

    def volume_up(self):
        if self.volume < Television.MAX_VOLUME:
            self.volume += 1
        else:
            self.volume = Television.MIN_VOLUME

    def volume_down(self):
        if self.volume > Television.MIN_VOLUME:
            self.volume -= 1
        else:
            self.volume = Television.MAX_VOLUME

    def __str__(self):
        return f"Power - {self.status}, Channel - {self.channel}, Volume - {self.volume}"
