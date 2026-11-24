from urllib import request

from fastapi import APIRouter, status, HTTPException, UploadFile, Form, File, Request
from pydantic import EmailStr
from starlette.responses import RedirectResponse, HTMLResponse

from data.image_storage import save_image
from data.db.operations.user_operation_db import create_user_db, read_all_users_db, read_one_user_db, update_user_db, delete_user_db
from enums.id_type import IdType
from models.user import UserBase, UserUpdate, UserID
from templating import templates

users_list:list[UserBase]=[]

router = APIRouter()

@router.get("/new")
def form_new_user(request: Request):
    return templates.TemplateResponse(request, "/users/new_user.html", {"title":"New User"})



@router.post("/", status_code=status.HTTP_201_CREATED, response_class=HTMLResponse)
async def create_user(
        first_name:str = Form(...),
        last_name: str = Form(...),
        id_type: IdType = Form(...),
        id_number: str = Form(...),
        phone_number: str = Form(...),
        email: EmailStr = Form(...),
        image: UploadFile = File()):
    '''
    Create a new users in the platform
    :param new_user:
    :return: OK, Created with status 201
    '''
    img_url = save_image(image, "users")
    new_user = UserBase(
        first_name=first_name,
        last_name=last_name,
        id_type=id_type,
        id_number=id_number,
        phone_number=phone_number,
        email=email,
        image_url=img_url
    )
    try:
        if create_user_db(new_user):
            return RedirectResponse("/users", status_code=status.HTTP_302_FOUND)
    except Exception as e:
        raise e



@router.get("/", status_code=status.HTTP_200_OK, response_model=list[UserID])
def show_all_users(request: Request):
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
        return RedirectResponse("/users/new", status_code=status.HTTP_302_FOUND)
        #raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No probe found")
    else:
        return templates.TemplateResponse(request, "/users/list.html",{"title":"Usuarios", "users":all_users})


@router.get("/{user_id}", status_code=status.HTTP_200_OK, response_model=UserID)
def show_one_user(user_id: int):
    '''
    Show one users in the platform
    :param user_id:
    :return: A users with the same ID registered
    '''
    ##if not users_list:
      #  raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No probe found")
    #elif len(users_list)<user_id:
     #   raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No probe found for list size")
    #else:
     #   for users in users_list:
      #      if users.id == user_id:
      #          return users
      #  return "User not found"
    #one_user=read_one_user_csv(user_id)
    #if not one_user:
    #    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No users found")
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
    Update a users in the platform
    :param user_id:
    :param new_user:
    :return: the new name of the users
    '''
    ##if not users_list:
      ##  raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No users found")
    #else:
     #   for users in users_list:
      #      if users.id == user_id:
       #         users.first_name = new_user.first_name
       #         return users
       # return None
    user = update_user_db(user_id, new_user)
    return user


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: str):
    '''    if users_list:
        for users in users_list:
            if users.id == user_id:
                users_list.remove(users)
                return users
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
    image_path = save_image(image, "users")
    return image_path







