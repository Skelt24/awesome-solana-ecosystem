import os
import re
import sys
from urllib.parse import urlsplit

# lychee counts redirects as successes, so a lost or hijacked domain that now forwards
# somewhere else passes silently. This fails the job when a link lands on another domain.

HOP = re.compile(r" --\[\d+\]--> ")


def site(url):
    host = urlsplit(url).hostname or ""
    # Last two labels: fine for this list's TLDs, but would treat a.co.uk and b.co.uk as one site.
    return ".".join(host.split(".")[-2:])


def main(report_path):
    with open(report_path, encoding="utf-8") as f:
        lines = f.read().splitlines()

    flagged = []
    for line in lines:
        if not line.startswith("* "):
            continue
        hops = HOP.split(line[2:])
        if len(hops) > 1 and site(hops[0]) != site(hops[-1]):
            flagged.append((hops[0], hops[-1]))

    if not flagged:
        print("No cross-domain redirects.")
        return 0

    section = [
        "",
        "## Cross-domain redirects",
        "",
        "These links now land on a different domain. Update the link if the project moved;"
        " remove the entry if the domain was lost or taken over.",
        "",
    ]
    section += [f"* {src} → {dst}" for src, dst in flagged]
    text = "\n".join(section) + "\n"

    for src, dst in flagged:
        print(f"::error::Cross-domain redirect: {src} -> {dst}")
    # Appended to lychee's report so the weekly issue includes it.
    for path in (report_path, os.environ.get("GITHUB_STEP_SUMMARY")):
        if path:
            with open(path, "a", encoding="utf-8") as f:
                f.write(text)
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
