from pyscript import document,display

# list of members that got in (case sensitive upon testing)
club_members = ["John Numbers", "Ben Franklin", "John Mark San Pedro Santos"]

def check_candidate(e):
    document.getElementById("output1").innerHTML = ""
    
    # combine first and last name
    first_name = document.getElementById("input1").value()
    last_name = document.getElementById("input2").value()
    full_name = f"{first_name} + {last_name}"
    
    # check if name is in the list of members that got in
    is_member = full_name in club_members
    
    # choose message based on result from checking the list of members that got in
    messages = [
        f"Sorry {full_name}, your name is not on the list.",
        f"Congratulations {full_name}! You are now part of the ICT club."
    ]
    
    result_message = messages[is_member]
    
    # Display message
    display(result_message, target="output1")
