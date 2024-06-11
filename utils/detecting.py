import cv2
import numpy as np

class DetectingCorner:
    
    def get_points(self,img,page):
        con = np.zeros_like(img)
        corners = []  # Initialize corners here
        # Loop over the contours.
        for c in page:
            # Approximate the contour.
            epsilon = 0.02 * cv2.arcLength(c, True)
            corners = cv2.approxPolyDP(c, epsilon, True)
            # If our approximated contour has four points
            if len(corners) == 4:
                break
            cv2.drawContours(con, c, -1, (0, 255, 255), 3)
            cv2.drawContours(con, corners, -1, (0, 255, 0), 10)
            # Sorting the corners and converting them to desired shape.
            corners = sorted(np.concatenate(corners).tolist())
                
        return corners
    def order_points(self, points):
        '''Rearrange coordinates to order:
        top-left, top-right, bottom-right, bottom-left'''
        if len(points) == 0:
            return []
        
        # Convert points to numpy array
        points = np.array(points, dtype='float32')
        
        # Calculate the centroid of the points
        centroid = np.mean(points, axis=0)
        
        # Calculate the angles of each point
        angles = np.arctan2(points[:,1] - centroid[1], points[:,0] - centroid[0])
        
        # Sort the points by angles
        rect = points[np.argsort(angles)]
        
        # Return the ordered coordinates
        return rect.astype('int').tolist()
    
    def get_destination(self,points):
        (tl, tr, br, bl) = points
        # Finding the maximum width.
        widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
        widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
        maxWidth = max(int(widthA), int(widthB))
        # Finding the maximum height.
        heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
        heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
        maxHeight = max(int(heightA), int(heightB))
        # Final destination co-ordinates.
        destination_corners = [[0, 0], [maxWidth, 0], [maxWidth, maxHeight], [0, maxHeight]]
        
        return self.order_points(destination_corners)

    def perspective_transform(self,destination_corners, corners, orig_img):

        # Getting the homography.
        M = cv2.getPerspectiveTransform(np.float32(corners), np.float32(destination_corners))
        # Perspective transform using homography.
        final = cv2.warpPerspective(orig_img, M, (destination_corners[2][0], destination_corners[2][1]), flags=cv2.INTER_LINEAR)

        return final