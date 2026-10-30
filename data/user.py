import csv
from models.user import UserBase, UserID

database = "probe.csv"

column_fields = ["id", "first_name", "last_name", "id_type", "id_number", "phone_number", "email"]

def write_into_csv(register: UserID):

    with open(database, "a", newline="") as csvfile:
        writer = csv.DictWriter(
            csvfile,
            column_fields,
        )
        writer.writerow(register.model_dump())
    csvfile.close()

def next_id():
    try:
        with open(database) as csvfile:
            reader = csv.DictReader(csvfile,column_fields)
            max_id = max(
                int(row["id"]) for row in reader
            )
            return max_id+1
    except (FileNotFoundError, ValueError):
        return 1




def create_user_register(new_user: UserBase):
    new_id = next_id()
    new_user_id = UserID(id=new_id, **new_user.model_dump())

    write_into_csv(new_user_id)
    return new_user_id


def read_all_users_csv():
    with open(database) as csvfile:
        reader = csv.DictReader(csvfile,column_fields)
        return [UserID(**row) for row in reader]


def read_one_user_csv(user_id: int):
    with open(database) as csvfile:
        reader = csv.DictReader(csvfile,column_fields)

        for row in reader:
            if int(row["id"]) == user_id:
                return UserID(**row)
        return None


def update_user_csv():
    #readoneuser
    #TODO implements the update user function
    pass

