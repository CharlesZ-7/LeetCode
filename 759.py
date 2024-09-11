class Solution:
    def employeeFreeTime(schedule):
        intervals = [time for employee in schedule for time in employee]
        intervals.sort(key=lambda x: (x[0], x[1]))
        work_time = [intervals[0]]

        for current in intervals[1:]:
            if work_time[-1][1] < current[0]:
                work_time.append(current)
            else:
                work_time[-1][1] = max(work_time[-1][1], current[1])

        free_time = []

        for i in range(1, len(work_time)):
            if work_time[i - 1][1] < work_time[i][0]:
                free_time.append([work_time[i - 1][1], work_time[i][0]])

        return free_time