#!/usr/bin/env python3

import sys
import datetime
import json

def main():
    rulesIn = [

    ]
    rules = []
    for entry in rulesIn:
        rules.append({
            "action": "deny",
            "direction": "outgoing",
            "priority": "regular",
            "process": "any",
            "remote-domains": entry.strip()
        })

    desc = "Source: https://blokada.org/blocklists/ddgtrackerradar/standard/hosts.txt | Domains: {} | Updated: {}".format(len(rules), datetime.datetime.now())
    root = {
        "description": desc,
        "name": "blokada_duckduckgo_tracker_radar",
        "rules": rules
    }

    print(json.dumps(root))

if __name__ == "__main__":
    main()
