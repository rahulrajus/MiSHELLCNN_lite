import os
import subprocess
corr = 0
total = 0
# for i in range(1,85):
#     fle_path = "tracks/not_track/" + "negative" +str(i).zfill(4)+".jpg"
#     print("python3 test.py " + fle_path)
#     # rslt = os.system("python3 test.py " + fle_path)
#
#     batcmd="python3 test.py " + fle_path
#     rslt = subprocess.check_output(batcmd, shell=True)
#     print("hi",str(rslt)[2])
#     if(str(rslt)[2] == "n"):
#         corr +=1
#         print(corr)
#     total+=1
for i in range(1,31):
    fle_path = "tracks/turtle_track/" + "track" +str(i).zfill(4)+".jpg"
    print("python3 test.py " + fle_path)
    # rslt = os.system("python3 test.py " + fle_path)
    batcmd="python3 overall_test.py " + fle_path
    rslt = subprocess.check_output(batcmd, shell=True)
    print("hi",str(rslt)[2])
    if(str(rslt)[2] != "n"):
        corr +=1
        print(corr)
    total+=1
print((0.0+corr)/total)
