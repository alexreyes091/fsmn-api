from sqlalchemy.orm import Session
#Locales
from app.database.models.users.user import UserAdress as model_adress
# from app.routes.schemas.users.user import UserAdress as shecma_adress

#querys
def getAll(db: Session):
    adress = db.query(model_adress).all()
    return adress

def getAdressById(id: int, db: Session):
    adress = db.query(model_adress).filter(model_adress.id_user == id).first()
    return adress