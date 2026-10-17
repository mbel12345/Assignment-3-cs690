"""Write exactly three pytest tests in this file.

Use only the public functions in ``reference``: reservation_disposition and
can_offer_to_waitlist. Do not edit the reference module. Call them with named
arguments, as in tests/test_reference_smoke.py.

Name each test so the acceptance criterion it checks is visible from the test
name or an adjacent comment, for example: def test_ac1_<what_it_checks>().

Put any policy value, such as the grace period, in a named constant marked as
a configured value, as in the at-risk example from the Week 5 lecture.
"""

from reference import can_offer_to_waitlist
from reference import reservation_disposition

GRACE_PERIOD = 15

def test_ac_1_reservation_is_held():

    status = reservation_disposition(minutes_after_start=GRACE_PERIOD-5, grace_minutes=GRACE_PERIOD, checked_in=False)
    assert status == "held"

def test_ac_2_reservation_is_released():

    status = reservation_disposition(minutes_after_start=GRACE_PERIOD+5, grace_minutes=GRACE_PERIOD, checked_in=False)
    assert status == "releasable"


def test_ac_3_can_be_offered_to_waitlist():

    status = can_offer_to_waitlist(disposition="releasable", preparation_complete=True)
    assert status == True
