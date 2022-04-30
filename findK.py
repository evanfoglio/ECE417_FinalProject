#!/usr/bin/python3
import sys
import numpy as np
import scipy.linalg
def findK(points1, points2) :
    arr = np.zeros((24,12))
    num_points = 24
    debug = False
    if debug:
        print("Points1:")
        print(points1)
        print("\n\n")
        print("points2:")
        print(points2)
        print("\n\n")
    
    all_points = np.concatenate((points1, points2), axis=0)
    if debug:
        print("all_points:")
        print(all_points)
        print("\n\n")



    square = 2.8 
    Xi = np.array([     [1*square, 1*square, 0, 1], [1*square, 2*square, 0, 1], [1*square, 3*square, 0, 1],
                        [2*square, 1*square, 0, 1], [2*square, 2*square, 0, 1], [2*square, 3*square, 0, 1],
                        [1*square, 0*square, 1*square, 1], [1*square, 0*square, 2*square, 1], [1*square, 0*square, 3*square, 1],
                        [2*square, 0*square, 1*square, 1], [2*square, 0*square, 2*square, 1], [2*square, 0*square, 3*square, 1]])

    if debug:
        print("Xi:")
        print(Xi)
        print("\nXi.shape")
        print(Xi.shape)
        print("\n\n")
    j = 0
    curr_index = 0
    for point in all_points:
        #Calculate needed variables
        # X Y Z
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
    
    if debug:
        print("arr.shape: " + str(arr.shape) + "\n\n")
        print("arr:")
        print(arr.__str__())
        print("\n\n")
    

    # Do the SVD
    u, s, vh = scipy.linalg.svd(arr)
    V = np.transpose(vh)
    
    if debug:
        print("s:")
        print(s)
        print("s.shape: " + str(s.shape))
        print("\n\n")

    if debug:
        print("u:")
        print(u)
        print("u .shape: " + str(u.shape))
        print("\n\n")





    # Strip off the last column 
    if debug:
        print("V[-1]:")
        print(V[11])
        print("V[-1] .shape: " + str(V[-1].shape))
        print("\n\n")
    
    P = V[-1].reshape(3,4)

    if debug:
        print("P:")
        print(P)
        print("\n\n")


    #P_stripped = np.delete(P, -1, -1)
    M = P[0:3,0:3]
    # QR Factorization
    K, R = scipy.linalg.rq(M)
    X = R * np.transpose(R)
    
    if debug:
        print("R:")
        print(R)
        print("\n\n")

        print("R*Rt:")
        print(X)
        print("\n\n")

        print("K*Kt:")
        Y = K * np.transpose(K)
        print(Y)
        print("\n\n")


    # print the K matrix
    print("K:")
    print(K)








