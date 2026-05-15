import math


class RankingService:

    def score(self, point, user_lat, user_lng):
        distance = math.sqrt(
            (point.latitude - user_lat) ** 2 +
            (point.longitude - user_lng) ** 2
        )

        return 1 / (distance + 0.001)