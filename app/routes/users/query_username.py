from sqlalchemy.orm import Session
#Locales
from app.database.models.users.user import UserAccount as model_account
# from app.routes.schemas.users.user import UserAccount as shecma_account

#querys
def getAll(db: Session):
    account = db.query(model_account).all()
    return adress

def getAccountById(id: int, db: Session):
    account = db.query(model_account).filter(model_account.id_user == id).first()
    return account