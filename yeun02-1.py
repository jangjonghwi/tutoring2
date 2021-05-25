
dc = {'새우깡': 700, '콘치즈': 850, '꼬깔콘': 750}

if '홈런볼' not in dc:
	dc['홈런볼'] = 900

print(dc)

for i in dc:
	dc[i] += 100

	
print(dc)

if '콘치즈' in dc:       # ‘콘치즈’ 있으면
    del dc['콘치즈']       # ‘콘치즈’ 삭제

print(dc)

if '치즈콘' not in dc:       # ‘치즈콘’ 없으면
    dc['치즈콘'] = 950       # ‘치즈콘’ 추가

print(dc)