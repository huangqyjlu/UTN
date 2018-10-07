# UTN urban traffic network

getArcGisShapeFiles.py

    It contains 2 functions:
        getChangchunDistricts(): get the ArcGis shapefiles for the districts of Changchun.
        getChangchunRoadnetwork(): get the ArcGis shapefiles for the road network of Changchun.
        the path of the shapefiles is './data'
    
matching.py

    It contains 1 functions:
        mapmatching(inpath, mapPath): 
            input is the path of the trajectory data, whic contains id, Longitude, latitude and time.
            mapPath is the path of the road network of Changchun (edges).
            

congestionStatistics.py
    It contains 1 functions:
        congestionStatistics(path): the path is the path of folder UTN.
    
