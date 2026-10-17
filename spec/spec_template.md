# Implementation-ready specification template

## Selected requirement

Requirement ID: P02, P06
Evidence trace: Student gives a reservation start time, then the end of the window is set based on a grace period defined by the manager, which can change.

## Behavior and scope

# Set reservation start and end time (start_time + grade_period) and set status, which could be of type Literal["reserved", "released"] to "reserved". Include the student id in the record that gets added to the database.


## Typed interface or function signature

```python
from datetime import datetime
def start_reservation(start_time: datetime, grace_period: int, student_id: int, kit_id: int) -> None:

```

## Preconditions

1. Grade period is non-negative. start_time is in the future. student_id is valid. kit_id is valid.

## Postconditions

1. Reservation record is added to the database, with non-empty start_time, end_time, student_id, and kit_id.

## Invariant

Each reservation can only have one status (it can not be reserved and released at the same time)

## Edge cases

1. Student is trying to reserve kit that a different student just reserved.
2. Grade period of 0

## Non-goal

State one behavior this specification explicitly does not cover.

## Settled decisions

1. It doesn't notify the student of their window, a different function will do this.

## Open questions the implementation agent may not answer

1. Which database or other data structure will store this information?
