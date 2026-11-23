# SW 1, Skills Test, PA2 codes
# Student Showcase
from pyscript import display, document

name = 'Leiane Jane Edos Gabia'
age = 15
height15 = 154.94
threecountries_to_visit = ['Japan', 'Australia', 'New Zealand']
student_type = False
about_me = {
    'color': 'Purple',
    'car_brand': 'Porsche',
    'shoe_size': 37,
    'best_friend': 'Bonnie and Alexa'
}
five_favorite_fruits = {'Mango', 'Banana', 'Lychee', 'Dalandan', 'Pineapple'}
seven_days = (
    'Monday', 'Tuesday', 'Wednesday', 'Thursday',
    'Friday', 'Saturday', 'Sunday'
)

display(type(name), target='result')
display(type(age), target='result')
display(type(height15), target='result')
display(type(threecountries_to_visit), target='result')
display(type(student_type), target='result')
display(type(about_me), target='result')
display(type(five_favorite_fruits), target='result')
display(type(seven_days), target='result')

document.getElementById('result').innerHTML = (
    f'Hello! My name is <i>{name}</i>.<br>'
    f'I am {age} years old. My height is {height15} cm.<br><br>'
    f'<b>Let me tell you about myself :)</b><br>'
    f'3 Countries I want to visit: {threecountries_to_visit}.<br>'
    f'It is {student_type} that I am a new student.<br>'
    f'Random things about me are: {about_me}.<br>'
    f'My favorite fruits are {five_favorite_fruits}.<br>'
    f'Lastly, all the days in the week are {seven_days}'
)


non_metals = {
    "H": {"name": "Hydrogen", "atomic_num": 1, "atomic_mass": "1.008"},
    "O": {"name": "Oxygen", "atomic_num": 8, "atomic_mass": "15.999"},
    "N": {"name": "Nitrogen", "atomic_num": 7, "atomic_mass": "14.007"},
    "C": {"name": "Carbon", "atomic_num": 6, "atomic_mass": "12.011"},
    "S": {"name": "Sulfur", "atomic_num": 16, "atomic_mass": "32.06"},
    "Cl": {"name": "Chlorine", "atomic_num": 17, "atomic_mass": "35.45"},
    "F": {"name": "Fluorine", "atomic_num": 9, "atomic_mass": "18.998"},
    "P": {"name": "Phosphorus", "atomic_num": 15, "atomic_mass": "30.974"},
    "Br": {"name": "Bromine", "atomic_num": 35, "atomic_mass": "79.904"},
    "I": {"name": "Iodine", "atomic_num": 53, "atomic_mass": "126.90"}
}


def check_element(e):
    document.getElementById("element-result").innerHTML = ""
    symbol = document.getElementById("element_symbol").value.strip()

    data = non_metals[symbol]
    display(f"Symbol: {symbol}", target="element-result")
    display(f"Element: {data['name']}", target="element-result")
    display(f"Atomic Number: {data['atomic_num']}", target="element-result")
    display(f"Atomic Mass: {data['atomic_mass']}", target="element-result")


grade_7 = {'Franco Deocampo', 'Sebastian Uclaray'}
grade_8 = {'Keane Pacaña', 'Almakram Arbison'}
grade_9 = {'Isabelle Cabatu', 'Nathan Bautista'}
grade_10 = {'Bonnie Nubla', 'Alexa Agnote'}


def create_order(event):
    first = document.getElementById('first_name').value
    last = document.getElementById('last_name').value

    new_member = {f"{first} {last}"}
    master_set = grade_7 | grade_8 | grade_9 | grade_10 | new_member

    document.getElementById('results').innerHTML = ""
    display(f'Full list of all members: {master_set}', target='results')
    display(f'Total number of members: {len(master_set)}', target='results')


creator_details = {
    "nickname": "LJ",
    "interests": "Sleeping, Eating, and ICT! \N{BLACK HEART SUIT} ",
    "hobbies": "Dancing, Sudoku, Running, and Going to the Gym",
    "dreams": threecountries_to_visit,
    "favorite_quote": "Wag magtipid sa pagkain."
}

document.getElementById("creator-profile").innerHTML = (
    f"<p><b>Name:</b> {name} (<i>{creator_details['nickname']}</i>)</p>"
    f"<p><b>Age:</b> {age}</p>"
    f"<p><b>Interests:</b> {creator_details['interests']}</p>"
    f"<p><b>Hobbies:</b> {creator_details['hobbies']}</p>"
    f"<p><b>Dreams & Travel:</b> {creator_details['dreams']}</p>"
    f"<p><b>Favorite Quote:</b> <i>\"{creator_details['favorite_quote']}\"</i></p>"
)