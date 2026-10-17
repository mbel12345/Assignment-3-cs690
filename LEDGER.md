# Provenance ledger

Use exactly this format for every entry. Write each entry when the work is done, one entry per reviewable change.

```text
## Entry <n>
artifact:  what this entry covers: a file, a commit SHA, a document, or an experiment
tool:      product name, model name, model version, and the date of use
prompts:   one-line summary each; the verbatim prompts live in prompts/ and are
           referenced here by file path
review:    what you read, what you changed, what you rejected, and why
checks:    the commands you ran and their results
evidence:  the requirement, test, or evidence ID this traces to
risk:      what remains unverified after this change

For an experiment, add three fields:
dataset:   task set identifier and its commit SHA or version
result:    metric, N, and the result table or its file path
changed:   what you did differently as a result
```

Add your entries below this line, starting with Entry 1.

---

## Entry 1
artifact: Part 3 of the report
tool: copilot in browser (2.20261015.61.0), 10/17/2026
prompts: Asked about INVEST would mean for requirement analysis for a reservation system. prompts/Entry_1.txt
review: It gave the acronym. I realized most of my requirements match the INVEST, based on this.
checks: n/a
evidence: Part 3, described if my requirements matched INVEST
risk: low risk, it was just for general guidance

## Entry 2
artifact: Part 4 of the report
tool: copilot in browser (2.20261015.61.0), 10/17/2026
prompts: Asked about what is an invariant in terms of a reservation system. prompts/Entry_2.txt
review: It listed some examples, including about preventing items from being double-booked. Similarly, I ended up deciding on talking about not having multiple statuses at once as it was more relevant to my other answers.
checks: n/a
evidence: Part 4, list an invariant established in the interview
risk: low risk, it was just for general guidance

## Entry 3
artifact: Part 6 of the report
tool: copilot in browser (2.20261015.61.0), 10/17/2026
prompts: Asked it to find ambiguity, incompleteness, and contraditions for the Interview.
review: It listed 8 examples, I then analyzed which of its concerns were valid (5 of 8 were)
checks: n/a
evidence: Part 6, list concerns for the interview that could affect requirement analysis
risk: Even with its response, AI still will probably try to guess requirements, even if you tell it to keep these issues in mind. Also, 3 of 8 were not fully accurate, so it is hard to trust this result fully.
