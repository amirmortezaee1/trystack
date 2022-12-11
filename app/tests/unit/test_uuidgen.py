import pytest 

from app.util import uuidgen 

def test_uuidgen():
     result = uuidgen()
     assert type(result) is str
     assert len(result) == 12
     assert result.isalnum() is True