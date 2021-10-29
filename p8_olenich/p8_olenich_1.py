import re
pose_estimation = input("Please, enter the test string: ")
pattern1 = re.compile(r"0\.\d+,\s0\.\d+")
pattern2 = re.compile(r"=0\.\d+")
points = re.findall(pattern1, pose_estimation, flags = 0)
points = str(points).replace("'","").replace("[","").replace("]","").replace(",","")
points = points.split(" ")
points = [float(i) for i in points]
scores = re.findall(pattern2, pose_estimation, flags = 0)
scores = [float(re.sub("=","",i)) for i in scores]
print("points =", points)
print("scores =", scores)