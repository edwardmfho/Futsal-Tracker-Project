import cv2

cap = cv2.VideoCapture('futsal2.mp4')

# create object detection instance
obj_detctor = cv2.createBackgroundSubtractorMOG2()

while True:

	ret, frame = cap.read()

	height, width, _ = frame.shape

	# print(height, width)
	roi = frame[ 230: 720, :]
	
	mask = obj_detctor.apply(roi)
	mask = cv2.dilate(mask, None)
	mask = cv2.GaussianBlur(mask, (9, 9), 0)

	_, mask = cv2.threshold(mask, 254, 255, cv2.THRESH_BINARY)
	contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

	for cnt in contours:

		# calculate area and remove small elements

		area = cv2.contourArea(cnt)

		if area > 45 and area < 80:
			#cv2.drawContours(roi, [cnt], -1, (0,255,0),2)
			x, y, w, h = cv2.boundingRect(cnt)
			cv2.rectangle(roi, (x, y), (x + w, y + h), (0, 255, 0), 3)


	# cv2.imshow('ROI', roi)
	cv2.imshow('Frame', frame)
	cv2.imshow('Mask', mask)

	key = cv2.waitKey(30)

	if key == 27:
		break

cap.release()
cv2.destroyAllWindows()