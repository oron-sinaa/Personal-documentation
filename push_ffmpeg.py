import subprocess
import csv
import multiprocessing

HOST_IP = "10.150.101.18"
TRANSPORT = 'tcp' #udp

def ensureFfmpeg(cmd):
    print("Here with a subprocess!" + cmd[-1])
    retval = 1
    while retval != 0:
        retval = subprocess.call(cmd)

def main():
    with open("/home/aanisnoor/Personal/Work/Misc/adani/RTSP_FEEDS.csv") as filereader:
        reader = csv.reader(filereader)
        numLines = 0
        cmds = []
        for line in reader:
            source, destiny = line[0], f"rtsp://{HOST_IP}:1935/live/{line[1]}"
            cmd = ['ffmpeg', '-re', '-rtsp_transport', f'{TRANSPORT}', '-i', f'{source}', '-c', 'copy', '-rtsp_transport', 'tcp', '-f', 'rtsp', f'{destiny}']
            cmds.append(cmd)
            numLines += 1
        pool = multiprocessing.Pool(processes=numLines)
        pool.map(ensureFfmpeg, cmds)

if __name__ == "__main__":
    main()
