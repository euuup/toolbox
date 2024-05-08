import time
import speedtest

# Speedtest--pip install speedtest-cli

def save_netspeed():
  """minute by minute saves"""
  
  # time flaf 
  time_flag = time.strftime("%Y-%m-%d %H:%M:%S")

  # Speedtest measure net speed
  st = speedtest.Speedtest()
  st.download()
  st.upload()

  # MB conversion
  d_spd = st.results.download / 1024 / 1024
  u_spd = st.results.upload / 1024 / 1024

  # save to csv
  with open("net_spd.csv", "a") as file:
    file.write(f"{time_flag},{d_spd:.2f},{u_spd:.2f}\n")

# minute by minute save to file
while True:
  save_netspeed()
  time.sleep(60)  # wait 60 seconds