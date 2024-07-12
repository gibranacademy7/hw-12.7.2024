user_id: str = str(input("Insert your id: "));
first_name: str = str(input("Insert your first name:"));
last_name: str = str(input("Insert your last name: "));
height: float = float(input("Insert your height: "));
birth_year: int = int(input("Insert your birth year: "));

print("f:user id: {user_id}");
print(f"first name: {first_name}");
print(f"last name: {last_name}");
print(f"height: {height}");
print(f"birth year: {birth_year}");

#or

print(f"user id: id - {user_id}, first name - {first_name}, last name {last_name}, height - {height}, birth year - {birth_year}: ");
