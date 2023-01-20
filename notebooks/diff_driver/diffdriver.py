import math

quadrants = [90, 180, 270, 360]

def angleInDegrees(x, y):
	answer = (math.atan2(y, x) * 180 / math.pi) + 90
	return answer if answer >= 0 else 360 + answer

class Driver:
	def __init__(self, maxMotorValue, scale, leftNegative, topNegative):
		self.maxMotorValue = maxMotorValue
		self.scale = scale
		self.leftNegative = leftNegative
		self.topNegative = topNegative

	def getDiffValues(self, x, y):
		# add a buffer for uncalibrated joysticks
		if scaledSpeed <= 0.1:
			return (0, 0)
		speed = (math.sqrt((x * x) + (y * y)) / 1)
		scaledSpeed = speed * (self.scale / (math.sqrt(self.scale ** 2)))
		travelAngle = angleInDegrees(x, y)
		# print(travelAngle)
		if travelAngle > 90 and travelAngle < 270:
			scaledSpeed = 0 - scaledSpeed
		for angle in quadrants:
			if travelAngle <= angle:
				prevAngle = angle - 90 if angle > 90 else 0
				bottomSplit = ((travelAngle - prevAngle) / 90)
				topSplit = 1 - bottomSplit
				break
		# constant angles:
		if travelAngle == 0:
			return (scaledSpeed, scaledSpeed)
		if travelAngle == 90:
			return (scaledSpeed, 0 - scaledSpeed)
		if travelAngle == 180:
			return (0 - scaledSpeed, 0 - scaledSpeed)
		if travelAngle == 270:
			return (0 - scaledSpeed, scaledSpeed)
		# specifics quadrants, order matters here
		if travelAngle < 90:
			return (scaledSpeed, scaledSpeed * topSplit)
		if travelAngle < 180:
			return (scaledSpeed, scaledSpeed * bottomSplit)
		if travelAngle < 270:
			return (scaledSpeed * topSplit, scaledSpeed)
		return (scaledSpeed * bottomSplit, scaledSpeed)
