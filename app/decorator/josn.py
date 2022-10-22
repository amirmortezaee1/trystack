from email import message
from functools import wraps
from fastapi import Header
from ..util import jsonify
def json_required(f, content_type: str = Header(...)):
     @wraps(f)
     def wrapper(*args, **kwargs):
          if content_type != "application.json":
               return jsonify(
                    metadata={
                         "message": "Content type is note supporte"
                    },
                    status=415,
               )
          else: 
               return f(*args, **kwargs)
     return wrapper