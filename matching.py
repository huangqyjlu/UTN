# coding=utf-8
'''
inpath: the path of the trajectory data.
mapPath: the path of shapefile for road network (edges).
'''
import os
import arcpy

def mapmatching(inpath, mapPath):
    
    newDirList = []
    fileList = []
    #get all filePath
    #inpath = r'.\04-10'
    for root, dirs, files in os.walk(inpath):
        for filename in files:
            fileList.append(os.path.join(root, filename))
        for dirname in dirs:
            newDirList.append(r'.\new_' + os.path.join(root, dirname)[2:])
    #creat new dir
    for nd in newDirList:
        if not os.path.exists(nd):
            os.makedirs(nd)
            
    #matching 
    print('creat map...')  
        
    #mapPath = r'.\roadNetwork\edges.shp' #the path of shapefile of edges in the road network.
    roadLayer = arcpy.MakeFeatureLayer_management(mapPath,'road_Lyr')
    
    for afile in fileList:
        print('matching ' + afile + '...')
        oldfile = open(afile)
        newfile = open(r'.\new_' + afile[2:], 'w')
        for line in oldfile:
            attrlist = line.split(',')
            point = arcpy.Point(float(attrlist[1]), float(attrlist[2]))
            pointGeometry = arcpy.PointGeometry(point)
            arcpy.SelectLayerByLocation_management(roadLayer, "WITHIN_A_DISTANCE", pointGeometry, "500 Meters")
            with arcpy.da.SearchCursor(roadLayer,["SHAPE@", "FID"]) as roads:
                minDistance = 100
                matchedID = ''
                for road in roads:
                    thisDistance = road[0].distanceTo(point)
                    if thisDistance < minDistance:
                        minDistance = thisDistance
                        matchedID = road[1]
                newfile.write(attrlist[0] + ',' + attrlist[1] + ',' + attrlist[2] + ',' + attrlist[3] + ',' + str(matchedID) + '\n')
        
        newfile.close()
        oldfile.close()
    print('**END**')
    
mapmatching(r'.\04-10',  r'.\roadNetwork\edges.shp')
