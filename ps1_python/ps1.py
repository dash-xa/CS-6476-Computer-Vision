# ps1
import cv2

# 1-a
img = cv2.imread('input/ps1-input0.png');  # already grayscale
# TODO: Compute edge image img_edges
img_edges = cv2.Canny(img, 0, 10)
cv2.imshow('edges', img_edges)
cv2.waitKey(0)
# cv2.imwrite(img_edges, 'output/ps1-1-a-1.png');  # save as output/ps1-1-a-1.png

# 2-a
# [H, theta, rho] = hough_lines_acc(img_edges);  # defined in hough_lines_acc.m
# TODO: Plot/show accumulator array H, save as output/ps1-2-a-1.png

# 2-b
# peaks = hough_peaks(H, 10);  # defined in hough_peaks.m
# TODO: Highlight peak locations on accumulator array, save as output/ps1-2-b-1.png

# TODO: Rest of your code here
