class Solution:
    def minAvailableDuration(slots1, slots2, duration):
        slots1.sort(key=lambda x: x[0])
        slots2.sort(key=lambda x: x[0])

        i = j = 0

        while i < range(len(slots1)) and j < range(len(slots2)):
            start = max(slots1[i][0], slots2[j][0])
            end = min(slots1[i][1], slots2[j][1])
            if end - start >= duration:
                return [start, start + duration]

            if slots1[i][1] < slots2[j][1]:
                i += 1
            else:
                j += 1

        return []

