# 1396. Design Underground System

# Medium

# Implement the UndergroundSystem class:

# void checkIn(int id, string stationName, int t)
# A customer with a card id equal to id, gets in the station stationName
# at time t.
# A customer can only be checked into one place at a time.

# void checkOut(int id, string stationName, int t)
# A customer with a card id equal to id, gets out from the station
# stationName at time t.

# double getAverageTime(string startStation, string endStation)
# Returns the average time to travel between the startStation and the
# endStation.
# The average time is computed from all the previous traveling from
# startStation to endStation that happened directly.
# Call to getAverageTime is always valid.
# You can assume all calls to checkIn and checkOut methods are
# consistent. If a customer gets in at time t1 at some station, they get
# out at time t2 with t2 > t1. All events happen in chronological order.


class UndergroundSystem:
    def __init__(self):
        self.passengers = {}
        self.routes = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.passengers[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.passengers[id]
        del self.passengers[id]
        route = startStation + stationName
        if route not in self.routes:
            self.routes[route] = [0, 0]
        self.routes[route][0] += t - startTime
        self.routes[route][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        route = startStation + endStation
        if route not in self.routes:
            return 0
        return self.routes[route][0] / self.routes[route][1]