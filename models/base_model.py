#!/usr/bin/python3
import uuid
from datetime import datetime
from models import storage
class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key,value in kwargs.items():
                if key == "__class__":
                    continue
                setattr(self, key, value)
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.fromisoformat(value))
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def save(self):
        storage.save()
        self.updated_at = datetime.now()

    def to_dict(self):
        dic_format = self.__dict__
        output = dict()
        for key in dic_format:
            if key == "created_at" or key == "updated_at":
                dic_format[key] = dic_format[key].isoformat()
            output[key] = dic_format[key]
        output["__class__"] = self.__class__.__name__
        return output

    def __str__(self):
        out = f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
        return out

