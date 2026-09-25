# Contributing

Thanks for helping keep this list useful. This is a **curated** list, not a directory — every
addition should make the ecosystem easier to navigate, not harder. Please read the criteria below
before opening a pull request.

## Inclusion criteria

An entry should meet **most** of the following before it's added:

- **Actively maintained.** Meaningful commits, releases, or product updates within the last 6
  months, or clear evidence of active usage (real TVL, real users, real transaction volume — not
  just a marketing site).
- **Solana-relevant.** Either Solana-native, or a multi-chain project with a genuine, functioning
  Solana deployment (not just a roadmap promise).
- **Not a known scam, rug, or exit.** No history of an unresolved exploit where user funds were
  not made whole, no DAO-voted shutdown, no abandoned domain now used for phishing.
- **Verifiable.** A live, working URL. Extraordinary claims (user counts, TVL, "the only X")
  should be supportable by a source a maintainer can check in under a minute.
- **Adds something distinct.** If a very similar, more established project is already listed,
  explain in the PR why this one earns its own entry (different niche, meaningfully different
  approach, etc.) rather than duplicating a category.

Security auditors, RPC/infra providers, and similar B2B tooling are held to the same bar: real,
checkable track record, not just a landing page.

## What gets removed

Entries are removed (not just tagged "inactive") when:
- The project has publicly shut down, been acquired and discontinued, or the DAO/team has voted
  to wind down.
- The domain has gone dark and/or is now used for something unrelated or malicious (phishing
  clones of dead wallet/exchange domains are a recurring pattern in this ecosystem — leaving the
  old link up is a risk to readers, not a neutral omission).
- The link has been broken for an extended period with no successor to point to.

If you're not sure whether something still qualifies, say so explicitly in the PR ("please
confirm — I couldn't verify current status") rather than silently keeping or dropping it.

## How to submit

1. Fork the repo and create a branch.
2. Add your entry to the most specific matching section, in the existing `- [Name](url) -
   description` format. Keep descriptions to one sentence and factual (no marketing superlatives
   you can't back up).
3. If you're removing or renaming something, explain why in the PR description with a source
   where possible (an announcement, a postmortem, an acquisition notice).
4. Open a pull request. A weekly automated link check runs against the whole list — if your PR
   introduces a link that's already broken, it will be flagged; fix it before requesting review.

## Style

- One entry per line, alphabetical order is not required but keep related projects grouped.
- Sections are organized by what the ecosystem actually looks like today, not by history — if
  your addition doesn't fit an existing section and represents a real category (5+ plausible
  future entries), propose a new one in the PR description.
