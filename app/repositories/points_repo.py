from app.models.point import Point
from app.core.database import SessionLocal


class PointsRepo:
    def save_many(self, points: list[Point]):
        db = SessionLocal()
        db.add_all(points)
        db.commit()
        db.close()

    def get_all(self):
        db = SessionLocal()
        return db.query(Point).all()