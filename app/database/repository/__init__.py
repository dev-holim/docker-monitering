from sqlalchemy.orm import Session
from app.database import SessionLocal, Base
from sqlalchemy import desc


class BaseRepository:
    def __init__(self, db: Session = SessionLocal):
        self.db = db
        self.model = Base

    def create(self, obj):
        try:
            self.db.add(obj)
            self.db.commit()
            self.db.refresh(obj)

            return obj.id
        except Exception as e:
            print(e)
            self.db.rollback()

    def delete(self, id: int):
        try:
            obj = self.find_by_id(id)
            if obj:
                self.db.delete(obj)
                self.db.commit()
                return True
            else:
                return False
        except Exception as e:
            print(e)
            self.db.rollback()

    def delete_multiple(self, ids: list[int]):
        try:
            for id in ids:
                obj = self.find_by_id(id)
                if obj:
                    self.db.delete(obj)

            self.db.commit()
        except Exception as e:
            print(f"Error while deleting IDs: {e}")
            self.db.rollback()
            return False

        return True

    def update(self, id: int, updates: dict):
        try:
            obj = self.find_by_id(id)
            if obj:
                for key, value in updates.items():
                    if hasattr(obj, key):
                        setattr(obj, key, value)
                self.db.commit()
                self.db.refresh(obj)
                return obj
            else:
                print(f"Object with id {id} not found.")
                return None
        except Exception as e:
            print(e)
            self.db.rollback()

    def find_by_id(self, id: int):
        try:
            return self.db.query(self.model).filter(id==self.model.id).first()
        except Exception as e:
            print(e)
            self.db.rollback()
