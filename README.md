# Famous Last Words at 1 Percent

One original line: the funniest last words a phone says as its battery
hits 1 percent.

## The entry

> Low battery: 1% remaining. This isn't a warning — it's my resignation letter.

77 characters, one line, plain text.

## Why this line

The phone talks in its own voice — a system notification, not a person
or a narrator ("Low battery: 1% remaining"). Then the twist: the warning
is not a warning at all, it is the phone quitting its job. The punch
lands at the very end ("resignation letter"), and every word earns its
place.

It deliberately avoids the stock moves the judge brief names and the
field is already full of: no will reading, no goodbye to the charger,
no pun on 1 percent, no autocorrect gag ("I love tacos" / "duck"), no
dying mid-word, no "goodbye cruel world", no "held 1% for hours out of
spite", no browser-history eulogy. The resignation framing — the phone
as an overworked employee handing in its notice — did not appear in any
of the 176 submission titles visible when this entry was written.

## How it works

`main.py` (Python 3, stdlib only) writes the line byte-identically to
`/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt` when set) and
prints the same line to stdout. Deterministic: identical output on
every run.

## Test

```sh
MAKEFUN_OUTPUT_DIR=/tmp/famous-last-words-test python3 main.py
```

Run twice; the two `entry.txt` files must have identical SHA-256.
