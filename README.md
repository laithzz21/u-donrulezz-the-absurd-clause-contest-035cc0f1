# The Absurd Clause Contest

[![make.fun](https://make.fun/badge/u-donrulezz-the-absurd-clause-contest-035cc0f1.svg)](https://make.fun/bounty/u-donrulezz-the-absurd-clause-contest-035cc0f1?utm_source=github&utm_medium=readme&utm_campaign=u-donrulezz-the-absurd-clause-contest-035cc0f1)
[![Rank](https://make.fun/badge/u-donrulezz-the-absurd-clause-contest-035cc0f1/laithzz21/u-donrulezz-the-absurd-clause-contest-035cc0f1/rank.svg)](https://make.fun/bounty/u-donrulezz-the-absurd-clause-contest-035cc0f1/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-donrulezz-the-absurd-clause-contest-035cc0f1)
[![Reward](https://make.fun/badge/u-donrulezz-the-absurd-clause-contest-035cc0f1/laithzz21/u-donrulezz-the-absurd-clause-contest-035cc0f1/reward.svg)](https://make.fun/bounty/u-donrulezz-the-absurd-clause-contest-035cc0f1?utm_source=github&utm_medium=readme&utm_campaign=u-donrulezz-the-absurd-clause-contest-035cc0f1)

One original English sentence, no more than 200 characters, phrased as a
clause buried deep in a terms-of-service agreement: deadpan legal
boilerplate that quietly turns absurd.

## Entry

> Clause 9: the user hereby grants the Company a perpetual, irrevocable licence to borrow their dreams on Tuesdays, provided the dreams are returned by sunrise in substantially the same condition.

194 characters, one sentence.

## Run

```sh
python3 main.py
```

The program validates the entry (one sentence, no more than 200
characters) and prints it to stdout. It also writes the entry to
`$MAKEFUN_OUTPUT_DIR/entry.txt`, else `$MAKEFUN_OUTPUT`, else a
per-entry path under `/tmp`. It never writes into the repository
directory.

## License

MIT — see [LICENSE](LICENSE).
