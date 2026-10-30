from fastapi import APIRouter, status, HTTPException, UploadFile

from data.image_storage import save_image
from data.db.operations.user_operation_db import create_user_db, read_all_users_db, read_one_user_db, update_user_db, delete_user_db
from models.user import UserBase, UserUpdate, UserID

users_list:list[UserBase]=[]

router = APIRouter()

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=UserID)
async def create_user(image: UploadFile, new_user: UserBase):
    '''
    Create a new user in the platform
    :param new_user:
    :return: OK, Created with status 201
    '''
    #users_list.append(new_user)
    #return {"New User Added": new_user}

    #return create_user_register(new_user)

    #new_user_id = UserID(id=new_id, **new_user.model_dump())
    ##image_path = save_image(image, "users")
    ##user = UserCreate(image_url=image_path, **new_user.model_dump())
    return create_user_db(new_user, image)



@router.get("/", status_code=status.HTTP_200_OK, response_model=list[UserID])
def show_all_users():
    '''
    Show all probe in the platform
    :return: List with whole probe registered
    '''

    #all_users = read_all_users_csv()
    #if not all_users:
     #   raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No probe found")
    #else:
     #   return all_users

    all_users = read_all_users_db()
    if not all_users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No probe found")
    else:
        return all_users


@router.get("/{user_id}", status_code=status.HTTP_200_OK, response_model=UserID)
def show_one_user(user_id: int):
    '''
    Show one user in the platform
    :param user_id:
    :return: A user with the same ID registered
    '''
    ##if not users_list:
      #  raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No probe found")
    #elif len(users_list)<user_id:
     #   raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No probe found for list size")
    #else:
     #   for user in users_list:
      #      if user.id == user_id:
      #          return user
      #  return "User not found"
    #one_user=read_one_user_csv(user_id)
    #if not one_user:
    #    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No user found")
    #else:
     #   return one_user

    one_user = read_one_user_db(user_id)
    if not one_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User not found")
    else:
        return one_user



@router.patch("/{user_id}", status_code=status.HTTP_200_OK, response_model=UserBase)
def update_user(user_id: str, new_user: UserUpdate):
    '''
    Update a user in the platform
    :param user_id:
    :param new_user:
    :return: the new name of the user
    '''
    ##if not users_list:
      ##  raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No user found")
    #else:
     #   for user in users_list:
      #      if user.id == user_id:
       #         user.first_name = new_user.first_name
       #         return user
       # return None
    user = update_user_db(user_id, new_user)
    return user


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: str):
    '''    if users_list:
        for user in users_list:
            if user.id == user_id:
                users_list.remove(user)
                return user
            return "User not found"
        return "User not found"
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No probe found")
'''
    deleted = delete_user_db(user_id)
    if not deleted:
        return "User not found... deleted done"
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User not found")


#Temporal
@router.post("/image", status_code=status.HTTP_201_CREATED)
def store_image(image:UploadFile):
    image_path = save_image(image, "probe")
    return image_path







