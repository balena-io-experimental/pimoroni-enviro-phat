#!/usr/bin/env python
# main.py

import sys, os, time, signal
from envirophat import light, weather, motion, analog

def signal_term_handler(signal, frame):
    # handle the sigterm signal and write that to a persisted file in /data
    with open("/data/signals.log","a+") as f:
        f.write('got SIGTERM')
    print 'got SIGTERM'
    sys.exit(0)

def signal_int_handler(signal, frame):
    with open("/data/signals.log","a+") as f:
        f.write('got SIGINT')
    print 'got SIGINT'
    sys.exit(0)

def signal_kill_handler(signal, frame):
    with open("/data/signals.log","a+") as f:
        f.write('got SIGKILL')
    print 'got SIGKILL'
    sys.exit(0)

# Register our signal handlers to clean up gracefully
signal.signal(signal.SIGTERM, signal_term_handler)
signal.signal(signal.SIGINT, signal_int_handler)
signal.signal(signal.SIGHUP, signal_kill_handler)

# Print all the available RESIN_* variables in the environment.
print "RESIN envvars\n"
for key in os.environ.keys():
    if 'RESIN' in key:
        print key,os.environ[key]

def write(line):
    sys.stdout.write(line)
    sys.stdout.flush()

write("--- Enviro pHAT Monitoring ---")

try:
    while True:
        rgb = light.rgb()
        analog_values = analog.read_all()

        output = """
Temp: {t}c
Pressure: {p}Pa
Light: {c}
RGB: {r}, {g}, {b}
Heading: {h}
Analog: 0: {a0}, 1: {a1}, 2: {a2}, 3: {a3}
""".format(
        t = round(weather.temperature(),2),
        p = round(weather.pressure(),2),
        c = light.light(),
        r = rgb[0],
        g = rgb[1],
        b = rgb[2],
        h = motion.heading(),
        a0 = analog_values[0],
        a1 = analog_values[1],
        a2 = analog_values[2],
        a3 = analog_values[3]
    )
        output = output.replace("\n","\n\033[K")
        write(output)
        lines = len(output.split("\n"))
        write("\033[{}A".format(lines - 1))

        time.sleep(1)

except KeyboardInterrupt:
    pass
