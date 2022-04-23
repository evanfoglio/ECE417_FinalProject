#!/usr/bin/python3
import sys
import numpy as np
def findK(points1, points2) :
    arr = np.zeros((8,12))
    num_points = 4
    
    np.append(points1, points2)

    j = 0
    curr_index = 0
    for point in points1:
        
        #Calculate needed variables
        Xi = np.array([[0, 0, 0, 1*2.8], [0, 1*2.8, 0, 1*2.8], [0, 0, 1*2.8, 1*2.8], [0, 0, 2*2.8, 1*2.8]])
        xip = point[0]
        yip = point[1]
        wip = 1
        
        neg_wiXit = -wip * Xi[j]
        yiXi = yip * Xi[j]
        wiXit = wip * Xi[j]
        neg_xiXit = -xip * Xi[j]


        # Calculate 2 rows at a time
        arr[curr_index][0] = 0
        arr[curr_index][1] = 0
        arr[curr_index][2] = 0
        arr[curr_index][3] = 0
        arr[curr_index][4] = neg_wiXit[0]
        arr[curr_index][5] = neg_wiXit[1]
        arr[curr_index][6] = neg_wiXit[2]
        arr[curr_index][7] = neg_wiXit[3]
        arr[curr_index][8] = yiXi[0]
        arr[curr_index][9] = yiXi[1]
        arr[curr_index][10] = yiXi[2]
        arr[curr_index][11] = yiXi[3]

        arr[curr_index+1][0] = wiXit[0]
        arr[curr_index+1][1] = wiXit[1]
        arr[curr_index+1][2] = wiXit[2]
        arr[curr_index+1][3] = wiXit[3]
        arr[curr_index+1][4] =0
        arr[curr_index+1][5] =0
        arr[curr_index+1][6] =0
        arr[curr_index+1][7] =0
        arr[curr_index+1][8] = neg_xiXit[0]
        arr[curr_index+1][9] = neg_xiXit[1]
        arr[curr_index+1][10] = neg_xiXit[2]
        arr[curr_index+1][11] = neg_xiXit[3]
        
        # Move to next two rows and move to next Xi value
        j = j + 1
        curr_index = curr_index + 2
    # Do the SVD
    u, s, vh = np.linalg.svd(arr, full_matrices=True)
    
    # Strip off the last column
    P = vh[-1].reshape(3,4)
    P_stripped = np.delete(P, -1, -1)

    # QR Factorization
    r, K = np.linalg.qr(P_stripped)
    
    # print the K matrix
    print(K)


