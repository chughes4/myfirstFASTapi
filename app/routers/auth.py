from fastapi import APIRouter, Depends, status, HTTPException, Response
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from .. import database, schemas, models, utils, oauth2

router = APIRouter(tags=['Authentication'])

@router.post('/login', response_model=schemas.Token)
def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):

    user = db.query(models.User).filter(models.User.email == user_credentials.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Creds")

    if not utils.verify(user_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid creds")

    access_token = oauth2.create_access_token(data= {"user_id": user.id})
    
    return {"access_token": access_token, "token_type": "bearer"}



    # {
    #     "title": "and another 4",
    #     "content": "this is to check user email",
    #     "published": true,
    #     "id": 5,
    #     "created_at": "2022-12-30T20:45:46.675143-05:00",
    #     "owner_id": 12,
    #     "owner": {
    #         "id": 12,
    #         "email": "first_user@email.com",
    #         "created_at": "2022-12-27T22:55:13.780562-05:00"
    #     }
    # },
    # {
    #     "title": "another ",
    #     "content": "The new content 10",
    #     "published": true,
    #     "id": 3,
    #     "created_at": "2022-12-30T20:12:00.562468-05:00",
    #     "owner_id": 13,
    #     "owner": {
    #         "id": 13,
    #         "email": "second_user@email.com",
    #         "created_at": "2022-12-30T17:57:12.561683-05:00"
    #     }