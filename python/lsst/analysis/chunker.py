### From fritz - 2021-06-29

from lsst.sphgeom import Box, Chunker, LonLat

# Get an sphgeom region representing a point of interest with coverage in DP0.1 DC2 dataset
somePointInDC2 = Box(LonLat.fromDegrees(60.0, -30.0))

# Use sphgeom "chunker" to find chunk parameters for chunk containing the point of interest
# Chunker construction arguments (stipes, substripes) are the partitioning parameters
# used when the data was ingested into Qserv
chunker = Chunker(numStripes=340, numSubStripesPerStripe=3)
chunk = chunker.getChunksIntersecting(somePointInDC2)[0]

# Use chunker to retrieve (spherical) bounding box for the identified chunk.
stripe = chunker.getStripe(chunk)
chunkInStripe = chunker.getChunk(chunk, stripe)
bounds = chunker.getChunkBoundingBox(stripe, chunkInStripe)

# Extract center and radius from bounding box.  Radius is half the minimum of box height
# and box width
center = bounds.getCenter()
coords = center.getLon().asDegrees(), center.getLat().asDegrees()
radius = min(bounds.getHeight().asDegrees(), bounds.getWidth().asDegrees()) / 2.0

print(f"center:{coords}, radius:{radius}")