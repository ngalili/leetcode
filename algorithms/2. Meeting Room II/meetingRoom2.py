# 253. Meeting Rooms II
# https://leetcode.com/problems/meeting-rooms-ii/

#Greedy method
def minMeetingRooms(intervals) -> int:
    rooms = []
    size = len(intervals)
    if size <= 1: return size
    sorted_intervals = sorted(intervals) # it's sorted by starting time
    rooms.append([sorted_intervals[0][1]]) #e0
    for i in range(1, size):
        booked = False
        for room in rooms:
            if sorted_intervals[i][0] >= room[-1]:
                room.append(sorted_intervals[i][1])
                booked = True
                break
        if not booked:
            rooms.append([sorted_intervals[i][1]])
    return len(rooms)

#Heap method - referred to Internet resources 
import heapq
def minMeetingRooms_(intervals) -> int:
    heap = []
    size = len(intervals)
    if size <= 1: return size
    sorted_intervals = sorted(intervals)

    for interval in sorted_intervals:
        if heap and interval[0] >= heap[0]:
            heapq.heappushpop(heap, interval[1])
        else:
            heapq.heappush(heap, interval[1])
    return len(heap)

if __name__ == "__main__":
    print(minMeetingRooms([[0, 30],[5, 10],[15, 20]]))
    print(minMeetingRooms([[6,15],[13,20],[6,17]]))
    print(minMeetingRooms_([[0, 30],[5, 10],[15, 20]]))
    print(minMeetingRooms_([[6,15],[13,20],[6,17]]))