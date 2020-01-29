#! /usr/bin/env python3

from cv2 import aruco

inToM = 0.0254

# Camera calibration info
maxWidthIn = 17
maxHeightIn = 23
maxWidthM = maxWidthIn * inToM
maxHeightM = maxHeightIn * inToM

charucoNSqVert = 6 #10
charucoSqSizeM = float(maxHeightM) / float(charucoNSqVert)
charucoMarkerSizeM = charucoSqSizeM * 0.7
# charucoNSqHoriz = int(maxWidthM / charucoSqSizeM)
charucoNSqHoriz = 9 #16

charucoDictionary = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)
#charucoDictionary = aruco.getPredefinedDictionary(aruco.DICT_4X4_100)
charucoBoard = aruco.CharucoBoard_create(
    charucoNSqHoriz,
    charucoNSqVert,
    .022, #.05275, #charucoSqSizeM,
    .0167, #.0265, #charucoMarkerSizeM,
    charucoDictionary)

perspectiveDictionary = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)
perspectiveBoard = aruco.CharucoBoard_create(
    3,  # We only want four corners for the perspective transform
    3,  # We only want four corners for the perspective transform
    charucoSqSizeM,
    charucoMarkerSizeM,
    perspectiveDictionary)

markerDictionary = aruco.getPredefinedDictionary(aruco.DICT_5X5_50)
#markerSizeIn = 5
markerSizeM = 0.015 #markerSizeIn * inToM

detectorParams = aruco.DetectorParameters_create()
detectorParams.cornerRefinementMaxIterations = 100
detectorParams.cornerRefinementMinAccuracy = 0.01
detectorParams.adaptiveThreshWinSizeMin = 3
detectorParams.adaptiveThreshWinSizeMax = 10
