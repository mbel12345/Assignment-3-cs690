# Evidence log schema

Use 8 to 10 entries. IDs must begin with E, A, or Q.

- E: real evidence from the interview transcript.
- A: an assumption that is not established by the interview.
- Q: an unresolved question that must be answered before the related decision is treated as settled.

Use this table shape:

| ID | Source | Claim | Status | Owner |
| --- | --- | --- | --- | --- |
| E-1 | INT-01:P09 | When a kit is released, they mark the reservation as released, and sometimes do things such as battery checks. | Stated | Coordinator |
| E-2 | INT-01:P02 | After a student makes a reservation, the technician pulls it from storage, checks the batteries and accessories, and attaches a paper reservation slip. | Stated | Coordinator |
| E-3 | INT-01:P21 | The waitlist should only see equipment that is ready to be given out. | Stated | Coordinator |
| A-1 | INT-01:P10 | The preferred method of contacing the sudents about their reservation going to the waitlist is unclear. | Assumption | Coordinator |
| A-2 | INT-01:P17 | Student does not know how the technicians communicate internally, and assumes a hold should stay in effect regardless of how it works internally. | Assumption | Student |
| Q-1 | INT-01:P07 | What is considered "a little late" when deciding when to release a kit? | Open | Coordinator |
| Q-2 | INT-01:P14 | What would be useful to show in the dashboard? | Open | Student |
| Q-3 | INT-01:P15 | How long of an extension would the "running late button" grant you, and would the student have to give an ETA? | Open | Student |


Status says how the claim is known: `Observed` for a specific past event someone described, `Stated` for a rule or fact a speaker asserted, `Assumption` for an A entry, and `Open` for a Q entry. Owner is the person or group who could confirm the claim or answer the question.

The worked row above is unrelated to the media-lab case. For this assignment, transcript sources must use the form `INT-01:Pxx`, for example `INT-01:P13`.

Do not cite `SYN-01` as real-user evidence. Synthetic-user material can generate a hypothesis, but it cannot establish actual user behavior, willingness, priorities, or requirements.
