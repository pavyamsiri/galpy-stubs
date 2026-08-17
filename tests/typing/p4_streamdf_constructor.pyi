from galpy.df.streamdf import streamdf

# Avoid expensive setup; this checks the public constructor boundary.
streamdf(0.01, nosetup=True)
