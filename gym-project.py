import json
import os
from datetime import datetime

DATA_FILE = "gym_data.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return {"members": {}}
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def register_member(data):
    member_id = input("Enter Member ID: ")
    if member_id in data["members"]:
        print("Member already exists.")
        return
    name = input("Enter Name: ")
    membership_type = input("Enter Membership Type (monthly/yearly): ").lower()
    payment = input("Enter Payment Amount: ")

    data["members"][member_id] = {
        "name": name,
        "membership": membership_type,
        "payment": float(payment),
        "check_ins": [],
        "check_outs": []
    }
    print(f"Member {name} registered successfully.")

def list_members(data):
    if not data["members"]:
        print("No members found.")
        return
    print("\n--- Member List ---")
    for mid, info in data["members"].items():
        print(f"ID: {mid} | Name: {info['name']} | Type: {info['membership']} | Paid: ${info['payment']}")

def check_in(data):
    member_id = input("Enter Member ID: ")
    member = data["members"].get(member_id)
    if not member:
        print("Member not found.")
        return
    time_now = datetime.now().isoformat()
    member["check_ins"].append(time_now)
    print(f"{member['name']} checked in at {time_now}")

def check_out(data):
    member_id = input("Enter Member ID: ")
    member = data["members"].get(member_id)
    if not member:
        print("Member not found.")
        return
    time_now = datetime.now().isoformat()
    member["check_outs"].append(time_now)
    print(f"{member['name']} checked out at {time_now}")

def view_member(data):
    member_id = input("Enter Member ID: ")
    member = data["members"].get(member_id)
    if not member:
        print("Member not found.")
        return
    print(f"\n--- Member Info ---")
    print(f"Name: {member['name']}")
    print(f"Membership: {member['membership']}")
    print(f"Total Paid: ${member['payment']}")
    print(f"Check-ins: {len(member['check_ins'])}")
    print(f"Check-outs: {len(member['check_outs'])}")

def main():
    data = load_data()
    while True:
        print("\n--- Gym Management ---")
        print("1. Register Member")
        print("2. List Members")
        print("3. Check In")
        print("4. Check Out")
        print("5. View Member Info")
        print("6. Save & Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            register_member(data)
        elif choice == "2":
            list_members(data)
        elif choice == "3":
            check_in(data)
        elif choice == "4":
            check_out(data)
        elif choice == "5":
            view_member(data)
        elif choice == "6":
            save_data(data)
            print("Data saved. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
