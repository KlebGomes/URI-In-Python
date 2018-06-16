seg = int(input())

min = seg // 60
hrs = min // 60
seg -= min * 60
min -= hrs * 60

print('{}:{}:{}'.format(hrs, min, seg))
