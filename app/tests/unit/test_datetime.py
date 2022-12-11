import pytest

from datetime import datetime

from app.util import now 

def test_now():
     result = now()
     # current_datetime = datetime.now()
     assert isinstance(result, datetime) is True
     assert hasattr(result, "year") is True
     assert hasattr(result, "month")
     assert hasattr(result, "day") is True
     assert hasattr(result, "weekday") is True
     assert hasattr(result, "minute") is True
     assert hasattr(result, "second") is True
     # assert datetime.year == current_datetime.year
     # assert datetime.month == current_datetime.month
     # assert datetime.day == current_datetime.day
     # assert datetime.weekday == current_datetime.weekday
     # assert datetime.minute == current_datetime.minute