from television import *
import pytest

def test_init():
        tv = Television()

        assert tv.channel == tv.MIN_CHANNEL
        assert tv.volume == tv.MIN_VOLUME
        assert tv.status == False
        assert tv.muted == False

def test_UpDown():
        tv = Television()

        tv.channel_up()
        tv.volume_up()
        assert tv.channel == 1
        assert tv.volume == 1

        tv.channel_down()
        tv.volume_down()
        assert tv.channel == 0
        assert tv.volume == 0

def test_Wrap():
        tv = Television()

        #wrap down
        tv.channel_down()
        tv.volume_down()
        assert tv.channel == tv.MAX_CHANNEL
        assert tv.volume == tv.MAX_VOLUME

        #wrap up
        tv.channel_up()
        tv.volume_up()
        assert tv.channel == tv.MIN_CHANNEL
        assert tv.volume == tv.MIN_VOLUME

def test_Bools():
        tv = Television()

        tv.power()
        tv.mute()
        assert tv.muted == True
        assert tv.status == True

        tv.power()
        tv.mute()
        assert tv.muted == False
        assert tv.status == False
