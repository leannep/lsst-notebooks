from collections import defaultdict
import re 

import lsst
from lsst.daf.butler import Butler 

config = 'dp02'
collection = '2.2i/runs/DP0.2'
butler = Butler(config, collections=collection)
registry=butler.registry

# Check dataset types exist
dataset_type_pattern = re.compile("^.*(calexp|coadd|catalog).*$")
allDatasetTypes = registry.queryDatasetTypes(dataset_type_pattern)
for x in allDatasetTypes:
    print(x)

groups = defaultdict(list)
for ref in registry.queryDatasets(dataset_type_pattern, collections=collection):
    groups[ref.datasetType.name].append(tuple(ref.dataId.values()))

for k, v in sorted(groups.items()):
    
f" N Data Ids: {len(v)}, N Distinct Data Ids: {len(set(v))} distinct data IDs" for k, v in sorted(groups.items())}

# retrieve a calexp
dataId = {'visit': 192350, 'detector': 175, 'band': 'i'}
calexp = butler.get('calexp', **dataId)
assert calexp is not None
assert type(calexp) == lsst.afw.image.exposure.ExposureF

# Retrieve a coadd
dataId = {'tract': 4431, 'patch': 17, 'band': 'i'}
datasetType = 'deepCoadd'
coadd = butler.get(datasetType, **dataId)
assert coadd is not None 
assert type(coadd) == lsst.afw.image.exposure.ExposureF

# retrieve a catalog 
datasetType = 'sourceTable'
dataId = {'visit': 192350, 'detector': 175}
src = butler.get(datasetType, dataId=dataId)
assert src is not None
f"Retrieved catalog of {len(src)} sources."