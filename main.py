from pyscript import document, display

my_list = ["Cassandra Mallari", "Madeline Narcisco", "Denie Manuntag", "Jiuliano Rivera"]

def show_list():
    output = document.getElementById("output")
    output.innerHTML = ""
    for item in my_list:
        display(item, target="output")

def get_full_name():
    # Grabs all inputs with id="user_input"
    inputs = document.querySelectorAll("#user_input")
    f_name = inputs[0].value.strip()
    l_name = inputs[1].value.strip()
    return f"{f_name} {l_name}".strip()

def clear_inputs():
    inputs = document.querySelectorAll("#user_input")
    for inp in inputs:
        inp.value = ""

def append_value(e):
    full_name = get_full_name()
    message = document.getElementById("message")

    if full_name:
        my_list.append(full_name)
        message.innerHTML = f"<span class='text-success'> Congratulations {full_name}! You are now part of the Communication Arts Club. </span>"
        show_list()
        clear_inputs()
    else:
        message.innerHTML = "<span class='text-warning'> Please enter a valid name. </span>"

def remove_value(e):
    full_name = get_full_name()
    message = document.getElementById("message")

    if full_name in my_list:
        my_list.remove(full_name)
        message.innerHTML = f"<span class='text-danger'> {full_name} removed from the list. </span>"
        show_list()
        clear_inputs()
    else:
        message.innerHTML = f"<span class='text-warning'> {full_name} is not in the member list.</span>"

show_list()