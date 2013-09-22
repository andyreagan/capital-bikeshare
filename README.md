This is my attempt to do something cool with DC's bike share data.

Need a sane way to test on smaller chunks of the data.
For the smaller data: (not a random sample)
head -n 1000 < data/... > test/data/...
And need to link the test/src to the src (want them to be copies)

Basic ideas:
-make a network of stations: stations as nodes and the rides as links
-happiness around bike riding: cool, but hard
    -have time of bike returns, location of the station returned
    -look at happiness of tweets near that?



