#!/usr/bin/env python3

import json
import os
import subprocess
from github import Github


def merge(event_info):
    pull_num = event_info["pull_request"]["number"]
    gh = Github(token=os.getenv("GITHUB_TOKEN"))
    owner = event_info["repository"]["owner"]["login"]
    reponame = event_info["repository"]["name"]
    repo = gh.get_repo(f"{owner}/{reponame}")
    pr = repo.get_pull(pull_num)
    if pr.mergeable:
        pr.merge()
    else:
        print(f"{pr} is not mergeable")


def tests_pass():
    status = subprocess.run(
        os.getenv("INPUT_TEST-COMMAND"),
        shell=True,
        check=False,
        cwd=os.getenv("GITHUB_WORKSPACE"),
    )
    return status.returncode == 0


def main():
    with open(os.getenv("GITHUB_EVENT_PATH", None), "r") as event_fd:
        event_info = json.load(event_fd)
    print(json.dumps(event_info, indent=2))
    if event_info["pull_request"]["user"]["login"] == "dependabot[bot]":
        if tests_pass():
            merge(event_info)
        else:
            sys.exit(f"'{os.getenv(INPUT_TEST-COMMAND)}' faied.")


if __name__ == "__main__":
    main()
