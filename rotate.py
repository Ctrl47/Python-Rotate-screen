import time, rotatescreen as rs
pd = rs.get_primary_display()
angel_list = [90, 0, 270, 180, 0, 270, 0, 180]
for i in range(30):
    for x in angel_list:
        pd.rotate_to(x)
        time.sleep(0.5)

# Enter (pip install rotate-screen) in Command Prompt
# After enter (pip install pywin32) in Command Prompt