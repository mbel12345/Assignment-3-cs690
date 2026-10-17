# Requirements Review Findings
**Case ID:** INT-01
**Domain:** University media equipment reservation and pickup

## 1. Conflicting Grace Period
- **Paragraph ID(s):** P06, P12
- **Excerpt:**
  - "The current policy is 15 minutes after the reservation start."
  - "The desk's rule is 20 minutes."
- **Defect Type:** Direct Contradiction
- **Unsafe Decision:** The implementation cannot safely determine when a reservation becomes eligible for release.

true positive; In P06 the staff says the period is 15 minutes, but in P12 student says she was told it was 20
---

## 2. Undefined Meaning of "Recorded Hold"
- **Paragraph ID(s):** P04, P06, P17, P19
- **Excerpt:**
  - "hold until 2:25"
  - "no recorded hold"
  - "staff have recorded that they are holding it"
- **Defect Type:** Ambiguity
- **Unsafe Decision:** It is unclear what actions, records, or system state constitute a valid hold and prevent release.

false positive; I think it is clear that staff can arbitrarily put it on hold, when they don't want to release it
---

## 3. Release Timing vs. Staff Discretion
- **Paragraph ID(s):** P06, P07
- **Excerpt:**
  - "At 15 minutes, if there is no check-in and no recorded hold, we can release the kit."
  - "If someone is only a little late, we try not to give the kit away."
- **Defect Type:** Ambiguity
- **Unsafe Decision:** The conditions under which staff may continue holding equipment after the release threshold are not defined.

false positive; it is clear that the staff should have the power to do this based on judgement and common sense, this is the correct behavior
---

## 4. Waitlist Eligibility Trigger Unclear
- **Paragraph ID(s):** P09, P10, P21
- **Excerpt:**
  - "They should get a message before it goes to the waitlist."
  - "The waitlist should only see equipment that is actually ready to hand out."
- **Defect Type:** Incompleteness
- **Unsafe Decision:** The event that makes equipment available to the waitlist and triggers notification is not specified.

true positive; there is no clear explanation of how the waitlist and notifications work
---

## 5. Ready Status Ownership Undefined
- **Paragraph ID(s):** P09, P17, P19, P21
- **Excerpt:**
  - "The technicians finish that check."
  - "I do not know what signal the technicians use internally."
  - "The equipment technicians need some way to mark the preparation step."
- **Defect Type:** Incompleteness
- **Unsafe Decision:** The source of truth and workflow for determining that a kit is ready for checkout are undefined.

true positive; staff is going over the paperwork process for the technicians to declare readiness, and it is a valid concern because he does not know the answer.
---

## 6. Check-In State Not Fully Specified
- **Paragraph ID(s):** P02, P17, P19, P21
- **Excerpt:**
  - "mark the reservation picked up"
  - "If I have already checked in at the desk"
  - "whether the student checked in"
- **Defect Type:** Ambiguity
- **Unsafe Decision:** It is unclear whether "checked in," "picked up," and "reservation completed" represent distinct states or the same state.

true positive; they go over the process of the student arriving at the desk, but don't clarify what these terms mean.
---

## 7. Manual Hold Extension Rules Missing
- **Paragraph ID(s):** P04, P19, P21
- **Excerpt:**
  - "hold until 2:25"
  - "reason for a manual hold"
  - "Staff sometimes extend a reservation after a student contacts us"
- **Defect Type:** Incompleteness
- **Unsafe Decision:** The criteria, authorization, and limits for creating or extending holds are not defined.

false positive; the manager has authority to make these decisions, and then input them into the system. That is not the responsibility of the system to decide when holds are allowed.
---

## 8. Future Feature Suggestions Mixed with Current-State Evidence
- **Paragraph ID(s):** P14, P15
- **Excerpt:**
  - "Honestly, a reservation dashboard that fixed all of this would be amazing."
  - "If there were a 'running late' button, I would probably use it every time I was delayed."
- **Defect Type:** Potential Requirements Contamination
- **Unsafe Decision:** An implementation team could incorrectly treat participant suggestions as validated requirements rather than evidence about the current process being studied.

true positive; this is a knee-jerk reaction where the student wants some extra feature that might not actually be relevant
