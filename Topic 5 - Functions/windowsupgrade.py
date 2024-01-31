def can_upgrade(memory, processor_speed, current_os):
 """Determines if a computer meets the requirements for a Windows 10 upgrade."""

 required_memory = 1
 required_processor_speed = 1
 allowed_operating_systems = ["Windows 7", "Windows 8"]

 return (
     memory >= required_memory and
     processor_speed >= required_processor_speed and
     current_os in allowed_operating_systems
 )

def main():
 """Gets user input and calls the can_upgrade function."""

 memory = float(input("Enter the current memory in your computer, in GB: "))
 processor_speed = float(input("Enter the current processor speed, in GHz: "))
 current_os = input("Enter the name of your current operating system: ")

 if can_upgrade(memory, processor_speed, current_os):
   print("Congratulations! Your computer can be upgraded to Windows 10.")
 else:
   print("Sorry, your computer does not meet the requirements for a Windows 10 upgrade.")

if __name__ == "__main__":
 main()
