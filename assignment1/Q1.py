agearray = [19,22,19,24,20,25,26,24,25,24]
agearray.sort()
minimumAge = min(agearray)
maximumAge = max(agearray)
agearray.append(minimumAge)
agearray.append(maximumAge)
agearray.sort()
length = len(agearray)
medianAge = agearray[ (length+1)//2] if length%2==1 else (agearray[length//2]+agearray[ (length//2)+1])/2
sumofAges = sum(agearray)
averageofAges = sumofAges//length
rangeofAges = maximumAge-minimumAge
print(minimumAge)
print(maximumAge)
print(medianAge)
print(averageofAges)
print(rangeofAges)