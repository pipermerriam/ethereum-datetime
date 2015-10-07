import pytest

@pytest.mark.parametrize(
    'timestamp,weekday',
    (
        (67737599, 3),
        (67737600, 4),
        (67823999, 4),
        (67824000, 5),
        (67910399, 5),
        (67910400, 6),
        (67996799, 6),
        (67996800, 0),
        (68083199, 0),
        (68083200, 1),
        (68169599, 1),
        (68169600, 2),
        (68255999, 2),
        (68256000, 3),
        (68342399, 3),
        (68342400, 4),
    ),
)
def test_get_weekday_from_timestamp(deployed_contracts, timestamp, weekday):
    crontab = deployed_contracts.DateTime
    assert crontab.getWeekday(timestamp) == weekday

