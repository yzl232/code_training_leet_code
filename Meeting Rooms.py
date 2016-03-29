'''


    Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.

    For example, Given [[0, 30],[5, 10],[15, 20]], return false.


'''
class Solution:
    def canAttendMeetings(self, arr):
        arr.sort(key=lambda i: i.start)
        return all(arr[i - 1].end <= arr[i].start for i in range(1, len(arr)))