import pytest

import datetime


@pytest.mark.parametrize(
    'dt,timestamp',
    (
        (datetime.datetime(1970, 1, 1), 0),
        (datetime.datetime(1970, 12, 31, 23, 59, 59), 31535999),
        (datetime.datetime(1971, 1, 1), 31536000),
        (datetime.datetime(2016, 2, 29, 23, 59, 59), 1456790399),
        (datetime.datetime(2016, 3, 1), 1456790400),
    ),
)
def test_dt_to_timestamp(deployed_contracts, dt, timestamp):
    crontab = deployed_contracts.DateTime
    assert crontab.toTimestamp(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second) == timestamp
