import time
run = input("Start? > ")
mins = 0
# Only run if the user types in "start"
if run == "start":
    # Loop until we reach 20 minutes running
    while mins != 1:
        print(">>>>>>>>>>>>>>>>>>>>>", mins)
        # Sleep for a minute
        time.sleep(60)
        # Increment the minute total
        mins += 1
    # Bring up final message
    print("1 minute has passed.")
