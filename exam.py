def processing_slips():
    totalstudentslate = 0
    current_ticket = int(input("What is the inital ticket number? \n"))  # Get the initial ticket number
    studentsinqueue = 0
    results = []
   
    while current_ticket > 0:
        action = input("Enter TAKE, HOF, SERVE, or CLOSE. \n")  # Get user action

        if action == "HOF":  # End the loop if HOF is entered
            break

        elif action == "TAKE":  # Increment counters when a student takes a ticket
            totalstudentslate += 1
            studentsinqueue += 1
            current_ticket += 1
            if current_ticket > 1000:  # Reset ticket number if over 1000
                current_ticket = 1

        elif action == "SERVE":  # Decrement queue when a student is served
            if studentsinqueue > 0:
                studentsinqueue -= 1

        elif action == "CLOSE":  # Log the current state and reset counters
            results.append(f"{totalstudentslate} {studentsinqueue} {current_ticket}")
            totalstudentslate = 0  # Reset late students count
            studentsinqueue = 0  # Reset queue count
            # current_ticket doesn't reset to 0 here; it continues based on the last TAKE
        
            for i in results:
                print(i)
            break
# Call the function
processing_slips()