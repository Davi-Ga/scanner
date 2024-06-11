import cv2
import numpy as np



class ImageProcessing:
    
    def resize_image(self, img, dim_limit):
        """Resizes the image to the specified dimension limit."""
        max_dim = max(img.shape)
        if max_dim > dim_limit:
            resize_scale = dim_limit / max_dim
            img = cv2.resize(img, None, fx=resize_scale, fy=resize_scale)
        return img
    
    def get_blank_page(self, img):
        """Performs morphological operations on the image to remove noise."""
        print('Getting blank page')
        kernel = np.ones((5,5),np.uint8)
        img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel, iterations= 3)
        return img

    def get_background(self, img):
        """Uses GrabCut algorithm to segment the foreground and background of the image."""
        print('Getting background')
        mask = np.zeros(img.shape[:2],np.uint8)
        bgdModel = np.zeros((1,65),np.float64)
        fgdModel = np.zeros((1,65),np.float64)
        rect = (20,20,img.shape[1]-20,img.shape[0]-20)
        cv2.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)
        mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
        img = img*mask2[:,:,np.newaxis]
        return img
    
    def enhance_image(self, img):
        """Enhances the image using histogram equalization."""
        print('Enhancing image')
        img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
        img_yuv[:,:,0] = cv2.equalizeHist(img_yuv[:,:,0])
        img_output = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)
        return img_output

    def edge_detection(self, img):
            """Converts the image to grayscale, applies Gaussian blur, and then performs edge detection using the Canny algorithm."""
            print('Detecting edges')
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            gray = cv2.GaussianBlur(gray, (11, 11), 0)
            canny = cv2.Canny(gray, 0, 200)
            canny = cv2.dilate(canny, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5)))
            return canny

    def get_contours(self, img, canny):
        """Finds and draws contours based on the edges detected by the Canny algorithm."""
        con = np.zeros_like(img)
        contours, hierarchy = cv2.findContours(canny, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
        page = sorted(contours, key=cv2.contourArea, reverse=True)[:5]
        con = cv2.drawContours(con, page, -1, (0, 255, 255), 3)
        return con,page

    def get_corners(self, img, page):
        """Identifies the corners of the largest contour."""
        print('Getting corners')
        corners = []
        for c in page:
            # Approximate the contour.
            epsilon = 0.02 * cv2.arcLength(c, True)
            approx = cv2.approxPolyDP(c, epsilon, True)
            # If our approximated contour has four points, we have found our corners.
            if len(approx) == 4:
                corners = approx
                break
        return corners