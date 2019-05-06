#!/usr/bin/env bash

import requests
from secrets import *
from pprint import pprint

r = requests.get('https://api.robinhood.com')