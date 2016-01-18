import glob
import numpy
import cv2
import re

def main():
	images = glob.glob("../server/uploads/*.jpg")
	imgList = []
	for img in images:
		value = re.search('(.*Img)([0-9]+).*?(.jpg)', img)
		val = int(value.group(2))
		imgList.append((img,val))
	imgList.sort(key=lambda x: x[1])
	fourcc = cv2.VideoWriter_fourcc(*'IYUV')
	shape = cv2.imread(imgList[0][0]).shape[:2]
	out = cv2.VideoWriter('testVideo.avi', -1, 20.0, shape, isColor=True)
	
	for img in imgList:
		frame = cv2.imread(img[0])
		out.write(frame)

	out.release()

if __name__ == "__main__":
	main()
