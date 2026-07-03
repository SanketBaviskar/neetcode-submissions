class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        times = [(target - pos)/time for pos, time in sorted(zip(position, speed))]
        count, leader_time = 0, 0
        for i in range(len(times)-1, -1, -1):
            if times[i] > leader_time:
                count += 1
                leader_time = times[i]
        return count