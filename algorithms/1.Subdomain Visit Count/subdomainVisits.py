# 811. Subdomain Visit Count
# https://leetcode.com/problems/subdomain-visit-count/

from typing import List
import collections
def subdomainVisits(cpdomains: List[str]) -> List[str]:
    res = collections.Counter()
    for domain in cpdomains:
        # cnt, subdomains = domain.split(" ")
        # cnt = int(cnt)
        # this approach is faster than using split
        cnt = int(domain[:domain.index(" ")])
        subdomains = domain[domain.index(" ")+1:]
        res[subdomains] += cnt
        for i, sub in enumerate(subdomains):
            if sub == ".":
                res[subdomains[i + 1 :]] += cnt
    return [str(cnt) + " " + domain for domain, cnt in res.items()]

if __name__ == "__main__":
    print(subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]))