#!/usr/bin/env bash

from Robinhood import Robinhood
import os

username = os.environ.get('RH_USERNAME')
password = os.environ.get('RH_PASSWORD')

client = Robinhood()
client.login(username=username, password=password)

client.logout()
