# This file allows quick switching of preset parameters

# strict onset = if true, ignores first slope if onset occured before event trigger/onset 
# plot = if true, plots each individual event
# ^^^ Best used if only looking at small number of data, otherwise
#     can be overwhelming
# startWindow = in seconds, when in event to begin analysis (create analysis window)
# endWindow = in seconds, how far from event end to stop analysis
# duration = in seconds, minimum duration for a slope to be considered valid; controls for noise
# minAmp = minimum amplitude to consider valid; controls for noise
# eventValue = value of the event during EDA recording

# Default values derived from findings of
#     Benedek, M. & Kaernbach, C., (2010) Decomposition of skin conductance data by means of
# nonnegative deconvolution. Psychopyshiology, 47(4)

profiles = {}

profiles[' Default'] = dict(
    strictOnset = True,
    startWindow = .5, # slightly lower than 3 SD's from mean onset
    endWindow = 5, # slightly more than 3 SD's onset + duration
    duration = .38, # slightly lower than 3 SD's from mean duration
    minAmp = 0.05
)

