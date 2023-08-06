# screen-switch
An example of an HTTP server that switches screen inputs by calling a DDC utility.

https://github.com/twstokes/screen-switch/assets/2092798/f49a8461-f656-490b-85a5-451604445e1a

## Problem

It's difficult or cumbersome to switch inputs using the controls on the monitors. An example might be where you have a multi-monitor setup and want to quickly and easily switch between a Mac and another computer.

## Solution

A web server runs on one of the machines with an interface allowing you to select a computer. This script is a really basic example of how this could be accomplished.

It could be adapted to work on any operating system, but in this case it expects the server to run on an M1 Mac.

## Installation
- Install [m1ddc](https://github.com/waydabber/m1ddc) ([Homebrew makes it easy](https://formulae.brew.sh/formula/m1ddc)) if using an Apple Silicon Mac as the server.
- Python 3 is required, and Flask should be installed by running `pip install -r requirements.txt` in the repo root.

## Setup
- The `switch_to_mac.sh` and `switch_to_pc.sh` shell scripts need to be updated to the appropriate number of displays and the input values.
  - If running on a machine that's not macOS or not Apple Silicon, this is where you'd substitute the `m1ddc` utility with something else.
  - If using `m1ddc`:
    - See [Commands section](https://github.com/waydabber/m1ddc#commands)
    - Keep in mind that this utility expects addresses to be decimal, not hex.
- `switcher.py`
  - Update or remove the `filter_ips()` hook.
  - Optionally update the port (defaults to 9000).

## Running
- `python3 switcher.py`
- Load the utility in a browser: `http://hostname:9000`
