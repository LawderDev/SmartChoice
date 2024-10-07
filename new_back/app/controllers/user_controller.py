from ..models.user import User
from app.database import DB

def get_user_by_id(user_id):
    user = DB.find_one("SELECT id, Nom, Prenom, Email, Password from Utilisateur WHERE id = ?", (user_id,))
    return User(user[0], user[1], user[2], user[3], user[4])