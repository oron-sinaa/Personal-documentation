import os
import csv
import subprocess
import multiprocessing

HOST_IP = os.environ.get("HOST_IP")
RTSP_PORT = os.environ.get("RTSP_PORT")
TRANSPORT = "tcp" #udp
CSV_PATH = "RTSP_FEEDS.csv"

def ensureFfmpeg(cmd):
    """
        * Makes sure stream restart in case of push failure.
        * Multiple instances can run.
    """
    print("[info] ffmpeg push subprocess [feed] " + cmd[-1])
    retval = 1
    # Restarts if process has not exited normally (with a passed terminate signal)
    while retval != 0:
        retval = subprocess.call(cmd, stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)

def main():
    """
        csv format (each line should with \\n):
        * rtsp://<user>:<pass>@<ip>:<port>,<streamname>.stream
    """
    with open(CSV_PATH) as filereader:
        reader = csv.reader(filereader)
        numLines = 0
        cmds = []
        # For every stream in csv
        for line in reader:
            source, destiny = line[0], f"rtsp://{HOST_IP}:{RTSP_PORT}/live/{line[1]}"
            cmd = ['ffmpeg', '-re', '-rtsp_transport', f'{TRANSPORT}', '-i', f'{source}', '-c', 'copy', '-b:v', '2M', '-rtsp_transport', 'tcp', '-f', 'rtsp', f'{destiny}']
            cmds.append(cmd)
            numLines += 1
        pool = multiprocessing.Pool(processes=numLines)
        pool.map(ensureFfmpeg, cmds)

if __name__ == "__main__":
    main()
