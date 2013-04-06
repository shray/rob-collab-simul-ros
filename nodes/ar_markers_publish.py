#!/usr/bin/env python

import rospy

import roslib
roslib.load_manifest('project_simulation')
import time

from geometry_msgs.msg import *
from project_simulation.msg import *
from visualization_msgs.msg import *
from std_msgs.msg import *
from random import random
from math import exp

import tf

#publish at Hz 
PUB_RATE = 30

#Human-Workspace
workspace = ['L0', 'L1', 'L2']

#possible locations
slocations = [ 
         { 'name' : 'L5' , 'position' : (-0.694954464364,0.264302079631,1.99317972681) , 'orientation' : (0.0864803654147,0.979654035105,-0.178136413992,0.0326578614002)},
         { 'name' : 'L3' , 'position' :  (-0.847151201376,0.297786050824,1.96464817216) , 'orientation' :  (0.099286275045,0.979143250933,-0.172672549803,0.040061456355)},
         { 'name' : 'L4' , 'position' : (-0.356133281188,0.200652416089,2.00604817833) , 'orientation' : (0.0864803654147,0.979654035105,-0.178136413992,0.0326578614002)},
         { 'name' : 'L6' , 'position' : (-0.526133281188,0.200652416089,2.00604817833) , 'orientation' : (0.0864803654147,0.979654035105,-0.178136413992,0.0326578614002)},

         { 'name' : 'L2' , 'position' : 
(-0.806263331563,-0.225740063166,2.17398472964), 'orientation' : 
  (0.0802827646415,0.978381335494,-0.188814418718,0.0259567976382)},
         { 'name' : 'L1' , 'position' : 
  (-0.663868350375,-0.237326254339,2.18771858991)
, 'orientation' : 
  (0.0831702389541,0.979029851475,-0.18352138094,0.0300526872406)},
         { 'name' : 'L0' , 'position' : 
  (-0.511209542213,-0.257163236559,2.18809949502)
, 'orientation' : 
(0.0864803654147,0.979654035105,-0.178136413992,0.0326578614002)
},
         { 'name' : 'L7' , 'position' : 
(0.738845303768,-0.216998119566,1.99359502486)
, 'orientation' : 
(-0.20227136896,0.962479020114,-0.179088366973,-0.025451639519)},
         { 'name' : 'L8' , 'position' : 
  (0.578156534057,0.0753144815163,1.88095830843)
, 'orientation' : 
(-0.155360904198,0.971362830021,-0.178368800013,-0.0224011848603)},
         { 'name' : 'L9' , 'position' : 
(0.394281491914,0.0255446236486,1.88485177488)
, 'orientation' : 
  (-0.168410139014,0.968065944316,-0.184818178623,-0.0181271449139)},

         { 'name' : 'L10' , 'position' : 
  (0.214970708732,-0.0341420080945,1.89436220148)
, 'orientation' : 
  (-0.167669713811,0.967651750635,-0.188267888617,-0.00959993117272)},
         { 'name' : 'L11' , 'position' : 
  (0.388313527453,-0.395303418346,2.04776721087)
, 'orientation' : 
  (-0.172801370397,0.967825570325,-0.181500892043,-0.0226003982657)},
         { 'name' : 'L12' , 'position' : 
  (0.588363257575,-0.288420043663,2.01260385776)
, 'orientation' :   (-0.201361148913,0.961335468405,-0.186586019109,-0.0217591904042)},
     { 'name' : 'L13' , 'position' : 
  (0.458363257575,-0.288420043663,2.01260385776)
, 'orientation' :   (-0.201361148913,0.961335468405,-0.186586019109,-0.0217591904042)}
         ]

bins_locs = [
    {'bin_id':2, 'location':'L0'}
    ,{'bin_id':3, 'location':'L1'}
    ,{'bin_id':11, 'location':'L2'}
    ,{'bin_id':10, 'location':'L3'}
    ,{'bin_id':12, 'location':'L4'}
    ,{'bin_id':7, 'location':'L5'}
    ,{'bin_id':14, 'location':'L6'}
    ,{'bin_id':15, 'location':'L7'}
    ,{'bin_id':13, 'location':'L8'}
    #,{'bin_id':16, 'location':'L9'}
    #,{'bin_id':17, 'location':'L10'}
    #,{'bin_id':18, 'location':'L11'}
    #,{'bin_id':19, 'location':'L12'}
    #,{'bin_id':20, 'location':'L13'}
    ]

#frame for markers
frame_of_reference = '/lifecam1_optical_frame'
#frame_of_reference = '/base_link'
#which bin is to be removed
bin_for_removal = None

#receive message to remove bin from publishing list
def bin_rmv(bin_to_rmv_msg):
    bin_to_rmv = bin_to_rmv_msg.data
    global bins_locs, bin_for_removal
    
    no_of_bins = bins_locs.__len__()
    
    for i in range(no_of_bins):
        if bins_locs[i]['bin_id']== bin_to_rmv:
            del bins_locs[i]
            bin_for_removal = bin_to_rmv
            return
    
    #incase it didn't return then bin was not found
    print "bin no: "+ str(bin_to_rmv) + "was not found"

def add_bin_id(bin_n_loc):
    global bins_locs
    temp_bin = {'bin_id':bin_n_loc.bin_id.data, 'location':bin_n_loc.location.data}
    bins_locs.append(temp_bin)
    return

def pub_workspace():
    global bins_locs, workspace
    work_bins = []

    for loc in workspace:
        for bin_loc in bins_locs:
            if bin_loc['location']==loc:
                work_bins.append(bin_loc['bin_id'])
                break

    work_msg  = std_msgs.msg.UInt8MultiArray()
    work_msg.data = work_bins
    return work_msg

def pub_bins():

    global bin_locs, slocations, PUB_RATE, bin_for_removal

    br = tf.TransformBroadcaster()
    
    pub = rospy.Publisher('ar_pose_marker', project_simulation.msg.AlvarMarkers)
    publish_work = rospy.Publisher('workspace_bins', std_msgs.msg.UInt8MultiArray)
    bin_rmv_sub = rospy.Subscriber('remove_bin', std_msgs.msg.UInt8, bin_rmv)
    bin_add_sub = rospy.Subscriber('add_bin', project_simulation.msg.bin_loc, add_bin_id)
    viz_pub = rospy.Publisher('ar_poses_visual', visualization_msgs.msg.MarkerArray)
    
    r = rospy.Rate(PUB_RATE)

    while not rospy.is_shutdown() :
        ar_markers = []
        ar_viz_markers = []

        for bin in bins_locs:

            marker = project_simulation.msg.AlvarMarker()
            marker.header.frame_id = frame_of_reference
            marker.pose.header.frame_id = frame_of_reference
            marker.id = bin['bin_id']

            temp_msg = visualization_msgs.msg.Marker()
            set_viz_marker(temp_msg, marker.id)
            temp_msg.id = marker.id
            
            for slocation in slocations:
                if slocation['name']==bin['location']:
                    marker.pose.pose.position.x = slocation['position'][0]
                    marker.pose.pose.position.y = slocation['position'][1]
                    marker.pose.pose.position.z = slocation['position'][2]
                    marker.pose.pose.orientation.x = slocation['orientation'][0]
                    marker.pose.pose.orientation.y = slocation['orientation'][1]
                    marker.pose.pose.orientation.z = slocation['orientation'][2]
                    marker.pose.pose.orientation.w = slocation['orientation'][3]

                    temp_msg.pose = marker.pose.pose
                    
                    br.sendTransform( slocation['position'], 
                                      slocation['orientation'], 
                                      rospy.Time.now(), 
                                      'Bin_'+str(bin['bin_id'])+'__'
                                                 +str(bin['location']), frame_of_reference)
                    '''#debug
                    print temp_msg
                    time.sleep(5)'''

                    #print marker
                    #time.sleep(1)
                    ar_markers.append(marker)
                    ar_viz_markers.append(temp_msg)

                    '''#debug
                    print ar_viz_markers
                    time.sleep(10)'''

        #add delete visual marker for bin removed
        if not bin_for_removal == None:
            temp_marker = gen_delete_bin(bin_for_removal)
            ar_viz_markers.append(temp_marker)
            bin_for_removal = None
                    
        #print markers
        #time.sleep(100)
        msg = project_simulation.msg.AlvarMarkers()
        msg.header.frame_id = frame_of_reference
        msg.markers = ar_markers
        #print msg
        #time.sleep(200)
        #break
        pub.publish(msg)
        
        '''#debug
        print ar_viz_markers
        time.sleep(40)'''
        
        #publish workspace
        publish_work.publish(pub_workspace())
        
        #publish visual markers
        viz_msg = visualization_msgs.msg.MarkerArray()
        viz_msg.markers = ar_viz_markers
        viz_pub.publish(viz_msg)
        
        r.sleep()
        
#return a visualization marker that deletes argument bin id
def gen_delete_bin(rmv_bin_id):
    temp_msg  = visualization_msgs.msg.Marker()
    temp_msg.id = rmv_bin_id
    temp_msg.header.stamp = rospy.Time()
    temp_msg.ns = 'marker_sim'
    temp_msg.action = visualization_msgs.msg.Marker.DELETE
    
    temp_msg.header.frame_id = frame_of_reference
    return temp_msg

    
def set_viz_marker(temp_msg, bin_id):
    marker_shape = visualization_msgs.msg.Marker.CUBE
    
    temp_msg.header.stamp = rospy.Time()
    temp_msg.ns = 'marker_sim'
    temp_msg.type = marker_shape
    temp_msg.action = visualization_msgs.msg.Marker.ADD
    
    temp_msg.header.frame_id = frame_of_reference
    
    temp_msg.color.r = 0.0#exp(-bin_id)
    temp_msg.color.g = 0.5#exp(-bin_id)
    temp_msg.color.b = 0.8#exp(-bin_id)
    temp_msg.color.a = 0.7#exp(-bin_id)
    
    temp_msg.scale.x = 0.05
    temp_msg.scale.y = 0.1
    temp_msg.scale.z = 0.03
    temp_msg.lifetime = rospy.Duration()
    return



#MAIN
if __name__ == '__main__':

    # init 
    rospy.init_node('ar_pose_markers_pub')

    pub_bins()
