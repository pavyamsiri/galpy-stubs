import numpy as np
from galpy.df.streamTrack import StreamTrack, StreamTrackPair

track = StreamTrack(np.linspace(0, 1, 3), np.ones((3, 3)), np.ones((3, 3)))
StreamTrackPair(track, track)
