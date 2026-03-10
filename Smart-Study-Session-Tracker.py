import time

start_time = None
current_subject = None
session_count = 0
minute = 60
subjects = []
session_durations = []


print("""
______________________________
Smart Study Session Tracker
******************************
1. Start study session       *
2. End study session         *
3. View study History        *
4. View total study time     *   
5. Exit.                     *
_____________________________*
""")

while True:
    choice = input("\nChoose an option (1-5): ")
    print()

    if choice == "1":
        if current_subject is not None:
            print("A study session is already running.")
        else:
            current_subject = input("What subject are you studying? ")
            start_time = time.time()
            print("Study session started...")

    elif choice == "2":
        if start_time is None:
            print("No study session has started yet.")
        else:
            end_time = time.time()
            session_duration = round(int((end_time - start_time) / minute))
            session_count += 1

            print("Study session ended.")
            print(f"You studied: {session_duration} minutes.")

            subjects.append(current_subject)
            session_durations.append(session_duration)

            start_time = None
            current_subject = None

    elif choice == "3":
        if len(session_durations) == 0:
            print("No history.")
        else:
            for x in range(len(subjects)):
                print(
                    f"Session: {x + 1} \nSubject: {subjects[x]} \nTime: {session_durations[x]} minutes.\n")

    elif choice == "4":
        if len(session_durations) == 0:
            print("No history.")
        else:
            total_study_time = 0

            for study_time in session_durations:
                total_study_time += study_time
                average_study_time = round(
                    total_study_time / len(session_durations))

            print(f"""
Total study time: {total_study_time}
Total session : {session_count}
Average study time: {average_study_time}
""")

    elif choice == "5":
        print("Goodbye. stay focused.")
        break

    else:
        print("Sorry, choose from the options.")
