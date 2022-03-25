# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 16:13:58 2022

@author: ASUS
"""
import pandas as pd

input_data=pd.read_csv('sample_srp_data.csv') #test_data_1.csv

sqr_S = (input_data.iloc[0,3])**2 + (input_data.iloc[0,4])**2
ship_name = []
for i in range(1,input_data.shape[0]):
    ship_name.append(input_data.iloc[i,0])
print(ship_name)

def findMinT(input_data):
    v_x = []
    v_y = []
    coord_x = []
    coord_y = []
    coord_x_support = input_data.iloc[0,1]
    coord_y_support = input_data.iloc[0,2]
    for i in range(1,input_data.shape[0]):
        coord_x.append(input_data.iloc[i,1])
        coord_y.append(input_data.iloc[i,2])
        v_x.append(input_data.iloc[i,3])
        v_y.append(input_data.iloc[i,4])
    
    a = []
    b = []
    c = []
    
    for i in range(len(coord_x)):
        a.append((v_x[i])**2 + (v_y[i])**2 - sqr_S)
        b.append(2*((coord_x[i] - coord_x_support)*(v_x[i]) + ((coord_y[i]-coord_y_support)*(v_y[i]))))
        c.append((coord_x[i] - coord_x_support)**2 + (coord_y[i]-coord_y_support)**2)
    
    results = []
    root = []
    for i in range(len(a)):
        d = b[i]**2 - 4*a[i]*c[i]
        if d > 0:  
            dummy = []
            dummy.append((-b[i] + d**(1/2))/(2*a[i]))
            dummy.append((-b[i] - d**(1/2))/(2*a[i]))
            if min([j for j in dummy if j >0], default = 0) != 0:
                root.append(min([j for j in dummy if j >0]))
            else:
                break
        elif d == 0:
            root.append(-b[i]/(2*a[i]))  
        else:  
            break
    if len(root) != 0:
        results.append(min(root))
        results.append(input_data.at[root.index(min(root))+1,'Name'])
        for k in range(len(coord_x)):
            coord_x[k]=coord_x[k] + v_x[k]*min(root)
            coord_y[k]=coord_y[k] + v_y[k]*min(root)
        
        coord_x_support = coord_x[root.index(min(root))]
        coord_y_support = coord_y[root.index(min(root))]
            
        coord_x.insert(0,coord_x_support)
        coord_y.insert(0,coord_y_support)
            
        input_data.update(pd.DataFrame({'x-coordinate': coord_x}))
        input_data.update(pd.DataFrame({'y-coordinate': coord_y}))
            
        input_data = input_data.drop(root.index(min(root))+1)
        input_data = input_data.reset_index(drop = True)
    else:
        None
    
    return results, input_data

def findPath(input_data):
    visited_ships = []
    unvisited_ships = []
    total_time = 0
    visited_ships.append(findMinT(input_data)[0][1])
    total_time=total_time + findMinT(input_data)[0][0]
    for i in range(input_data.shape[0]):
        results = []
        input_data = findMinT(input_data)[1]
        results.append(findMinT(input_data)[0])
        if len(findMinT(input_data)[0]) == 0:
            break
        for j in results:
            visited_ships.append(j[1])
            total_time=total_time + j[0]
    for i in ship_name:
        if i not in visited_ships:
            unvisited_ships.append(i)
    return visited_ships, unvisited_ships, total_time, input_data

print(findPath(input_data))