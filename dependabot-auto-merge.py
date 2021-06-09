#!/usr/bin/env python3

import argparse
import os
from github import Github

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('token', help='Github token')
