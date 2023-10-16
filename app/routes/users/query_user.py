from sqlalchemy.orm import Session, joinedload
#Locales
from app.database.models.users.user import User as model_user

# QUERYS USER
# -------------------------------------------------------------
def getAll(db: Session):
    user = db.query(model_user).all()
    return user

def getUserById(id_user: int, db: Session):
    if isUserExist(id_user, db):
        user = (
            db.query(model_user)
            .filter(model_user.id_user == id_user)
            .first()
        )
        return user
    return None
# -------------------------------------------------------------


# VALIDACIONES
# -------------------------------------------------------------
def isUserExist(id_user: int, db: Session):
    user =(
        db.query(model_user).
        filter(model_user.id_user == id_user)
        .first()
    ) 
    return user is not None