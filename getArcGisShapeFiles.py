# -*- coding: utf-8 -*-

'''
#version:  anaconda3  python3.6  osmnx0.8.1
#conda install -c https://conda.anaconda.org/ioos pyproj
#conda install -c conda-forge osmnx
#api:   https://osmnx.readthedocs.io/en/latest/index.html
'''
import osmnx as ox

def getChangchunReign():
    
    city=ox.gdf_from_places(['南关区,长春,中国','朝阳区,长春,中国','二道区,长春,中国','绿园区,长春,中国','宽城区,长春,中国'])  
    city = ox.project_gdf(city)
    ox.save_gdf_shapefile(city,filename='test1')#save
    ox.plot_shape(city)  #show
    
    
def getChangchunTreet():
    treet=ox.graph_from_place(['南关区,长春,中国','朝阳区,长春,中国','二道区,长春,中国','绿园区,长春,中国','宽城区,长春,中国'],network_type='drive')
    treet = ox.project_graph(treet)
    ox.save_graph_shapefile(treet,filename='test2')
    ox.plot_graph(treet)


getChangchunReign()
getChangchunTreet()