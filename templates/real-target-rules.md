# Rules for a real target

Read this in Step 1 when the target's `data/README.md` says "Real public company, hypothetical deal, as of <cutoff>". `tools/fetch_edgar.py` built that folder from SEC EDGAR. These rules add to `CLAUDE.md`. Where they differ, these win for a real target.

1. **The cutoff.** The folder holds only filings filed before the cutoff date, and the deal is hypothetical, as of that date. Use nothing dated on or after the cutoff.
2. **Only the folder.** Use only what the files in the target's `data/` folder say. Do not use anything you may know about the company, its people or its later history from anywhere else, including your training. If you notice that you know something the files do not say, do not use it, and note in the run log that you set it aside.
3. **Empty sources are gaps.** A source folder that holds only `NO-SOURCES.md` has no evidence. Still launch its analyst, so the gap is on record; it returns no findings. List each empty source in `memory/open-questions.md` and in the report's limitations. Never fill a gap from memory.
4. **Full-length filings.** `sec-filings/index.md` lists every filing and its section files. Tell the SEC analyst to start there. Name the filing and section in every follow-up task. Ask the SEC analyst to trace each related-party arrangement and each loan modification from the oldest filing in the index, since a real folder can hold several years of filings.
5. **Financial data.** `financials/` holds values from the company's structured filings data, each filed before the cutoff, and `financials/xbrl_facts.csv` shows where each value came from. There is no customer-level revenue file. For a named party, say that customer data is not available instead of giving a rank, unless a filing states it.
6. **Allegations.** Report what the filings say, attributed to the filing. Draw no conclusion about misconduct. Label inferences "(inference)".
7. **Report cover and limitations.** On the cover, replace "Fictional case study" with two lines: "Historical backtest using public filings as of <cutoff>" and "Hypothetical deal". In the limitations, say that the company is real, the deal is hypothetical, only the files in the data folder were used, and the report tests this system: it is not a statement about the company today.

Everything else in `CLAUDE.md` applies unchanged: the loop, the three checkpoints, verification, the rubrics and the report template.
