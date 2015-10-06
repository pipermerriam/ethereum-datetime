import pytest

@pytest.mark.parametrize(
    'timestamp,weekday',
    (
        (67737599, 2),
        (67737600, 3),
        (67823999, 3),
        (67824000, 4),
        (67910399, 4),
        (67910400, 5),
        (67996799, 5),
        (67996800, 6),
        (68083199, 6),
        (68083200, 0),
        (68169599, 0),
        (68169600, 1),
        (68255999, 1),
        (68256000, 2),
        (68342399, 2),
        (68342400, 3),
    ),
)
def test_get_weekday_from_timestamp(deployed_contracts, timestamp, weekday):
    crontab = deployed_contracts.DateTime
    assert crontab.getWeekday(timestamp) == weekday

