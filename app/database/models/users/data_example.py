from app.database.models.users.user import User, UserAccount, UserAdress
from app.routes.schemas.users.role import RoleType
from app.database.config import SessionLocal

# Carga de datos incial
def init_db():
    db = SessionLocal()
    # Instancias de datos
    user = seed_users()
    account = seed_user_account()
    adress = seed_user_adress()
    # Carga de datos
    db.add_all(user)
    db.add_all(account)
    db.add_all(adress)
    db.commit()

# Semilla de datos iniciales
def seed_users():
    users = [
        User(id_user=1001, first_name='Roberto Ramirez', last_name='Hernandez', role=RoleType.COLABORADOR, avatar='https://d2u8k2ocievbld.cloudfront.net/memojis/male/1.png'),
        User(id_user=1002, first_name='Stefy', last_name='Cruz Sua', role=RoleType.COLABORADOR, avatar='https://d2u8k2ocievbld.cloudfront.net/memojis/female/1.png'),
        User(id_user=1003, first_name='Denis Dario', last_name='Cuadrado', role=RoleType.COLABORADOR, avatar='https://d2u8k2ocievbld.cloudfront.net/memojis/female/2.png'),
        User(id_user=1004, first_name='Esteban Emilio', last_name='Contreras', role=RoleType.COLABORADOR, avatar='https://d2u8k2ocievbld.cloudfront.net/memojis/female/2.png'),
        User(id_user=1005, first_name='Patric Pavaroti', last_name='Lau', role=RoleType.COLABORADOR, avatar='https://d2u8k2ocievbld.cloudfront.net/memojis/male/2.png'),
        User(id_user=1006, first_name='Sander Solovino', last_name='Dog', role=RoleType.COLABORADOR, avatar='https://d2u8k2ocievbld.cloudfront.net/memojis/female/3.png'),
        User(id_user=1007, first_name='Pedro Peralta', last_name='Cornejo', role=RoleType.COLABORADOR, avatar='https://d2u8k2ocievbld.cloudfront.net/memojis/male/3.png'),
        User(id_user=1008, first_name='Alexis Arveloa', last_name='Wong', role=RoleType.COLABORADOR, avatar='https://d2u8k2ocievbld.cloudfront.net/memojis/male/4.png'),
        User(id_user=1009, first_name='Antonela Bu', last_name='Lau', role=RoleType.COLABORADOR, avatar='https://d2u8k2ocievbld.cloudfront.net/memojis/female/4.png'),
        User(id_user=1010, first_name='Henrry Dario', last_name='Perez', role=RoleType.COLABORADOR, avatar='https://d2u8k2ocievbld.cloudfront.net/memojis/male/5.png'),
        User(id_user=1011, first_name='Duglas', last_name='Crua Wong', role=RoleType.COLABORADOR, avatar='https://d2u8k2ocievbld.cloudfront.net/memojis/female/5.png'),
        User(id_user=1012, first_name='William Josue', last_name='Chevez', role=RoleType.COLABORADOR, avatar='https://d2u8k2ocievbld.cloudfront.net/memojis/female/5.png'),
        User(id_user=1013, first_name='Ever Josue', last_name='Singua', role=RoleType.COLABORADOR, avatar='https://d2u8k2ocievbld.cloudfront.net/memojis/male/7.png'),
        User(id_user=1014, first_name='Sara', last_name='Herrera Chi', role=RoleType.COLABORADOR, avatar='https://d2u8k2ocievbld.cloudfront.net/memojis/female/5.png'),
        User(id_user=1015, first_name='Martha Cecilia', last_name='Cetino', role=RoleType.COLABORADOR, avatar='https://d2u8k2ocievbld.cloudfront.net/memojis/female/7.png'),
        User(id_user=1016, first_name='Nahun Alexander', last_name='Amador', role=RoleType.COLABORADOR, avatar='https://d2u8k2ocievbld.cloudfront.net/memojis/female/8.png'),
        User(id_user=1017, first_name='Frank', last_name='Sarmiento', role=RoleType.COLABORADOR, avatar='https://d2u8k2ocievbld.cloudfront.net/memojis/female/5.png'),
        User(id_user=1018, first_name='Lexi', last_name='Lipa', role=RoleType.COLABORADOR, avatar='https://d2u8k2ocievbld.cloudfront.net/memojis/female/9.png'),
        User(id_user=1019, first_name='Donatelo', last_name='Tortoise', role=RoleType.COLABORADOR, avatar='https://d2u8k2ocievbld.cloudfront.net/memojis/female/5.png'),
        User(id_user=1020, first_name='Leti Sevitar', last_name='Flamenco', role=RoleType.COLABORADOR, avatar='https://d2u8k2ocievbld.cloudfront.net/memojis/male/11.png'),
        User(id_user=2001, first_name='Debora', last_name='Flamenco', role=RoleType.MANAGER, avatar='https://d2u8k2ocievbld.cloudfront.net/memojis/male/7.png'),
        User(id_user=2002, first_name='Lester Andres', last_name='Chevez', role=RoleType.MANAGER, avatar='https://d2u8k2ocievbld.cloudfront.net/memojis/female/5.png'),
    ]
    return users

def seed_user_account():
    users_account = [
        UserAccount(id_user=2001, username='debora.flamenco', password='$2b$12$aKj1j6PU1.vzNRYqlMGu2uFzfJ7Mbjz5E7Rtl/JfvRburKRTIAnyi', is_active=True),
        UserAccount(id_user=2002, username='lester.chevez', password='$2b$12$aKj1j6PU1.vzNRYqlMGu2uFzfJ7Mbjz5E7Rtl/JfvRburKRTIAnyi', is_active=True),
    ]
    return users_account

def seed_user_adress():
    users_adress = [
        UserAdress(id_user=1001, description='Barrio las acacias entre 14 y 15 calle, 2 avenida.', coordinate='-88.0220350815384,15.51724767337923'),
        UserAdress(id_user=1002, description='Bo Paz Barahona, 11 avenida 12 y 13 calle', coordinate='-88.03223917839824,15.497103463284418'),
        UserAdress(id_user=1003, description='Polideportivo de la Villa Olimpica, 2do Anillo', coordinate='-88.0026821463577,15.471257275300118'),
        UserAdress(id_user=1004, description='Mexichem Amanco, Carretera haci San Pedro Sula', coordinate='-87.98751374850804,15.559867493659311'),
        UserAdress(id_user=1005, description='Chamelecón, San Pedro Sula, Cortés, Honduras', coordinate='-88.01631861741664,15.426183566794776'),
        UserAdress(id_user=1006, description='IPSA, San Pedro Sula, Cortés, Honduras', coordinate='-88.01129336858716,15.502865274546906'),
        UserAdress(id_user=1007, description='Pollos Vila, Col. Aurora, San Pedro Sula', coordinate='-88.01152117073487,15.499482148076709'),
        UserAdress(id_user=1008, description='Plaza Uno, Salida a La Lima, San Pedro Sula', coordinate='-88.00922378908422,15.501660763409717'),
        UserAdress(id_user=1009, description='Modelo, Col modelo, San Pedro Sula', coordinate='-88.01084423858985,15.51468969611939'),
        UserAdress(id_user=1010, description='CrossfitSPS, San Pedro Sula', coordinate='-88.04579123507853,15.522681574370694'),
        UserAdress(id_user=1011, description='Blvd del Sur, frente a Grupo Q ', coordinate='-88.033970920553,15.487677571263205'),
        UserAdress(id_user=1012, description='El Oconillo, Choloma, Cortés, Honduras', coordinate='-87.92903554550053,15.542407697005174'),
        UserAdress(id_user=1013, description='Peaje Blvd del Este, La Lima, Cortés', coordinate='-87.96254832569817,15.459443621804937'),
        UserAdress(id_user=1014, description='Estadio Yankel Rosenthal, San Pedro Sula', coordinate='-87.99731715608688,15.488193557447687'),
        UserAdress(id_user=1015, description='HanesInk, Zip Indehlva, Choloma', coordinate='-87.96034570493654,15.613331576726793'),
        UserAdress(id_user=1016, description='Texaco Dox Choloma, Autopista CA-5', coordinate='-87.95738041148915,15.608156765331529'),
        UserAdress(id_user=1017, description='ELCATEX, Choloma, Cortés', coordinate='-87.9628294550036,15.605154338487111'),
        UserAdress(id_user=1018, description='Kilómetro 45, Puerto Cortés', coordinate='-87.80903115499268,15.694369059226545'),
        UserAdress(id_user=1019, description='Toloa Creek, Puerto Cortés', coordinate='-87.7786903150873,15.720238850632171'),
        UserAdress(id_user=1020, description='Gasolinera UNO, Frente a Carretera, Omoa', coordinate='-88.03594723013121,15.777128295021129'),
        UserAdress(id_user=2001, description='Mexichem Amanco, Carretera haci San Pedro Sula', coordinate='-87.98751374850804,15.559867493659311'),
        UserAdress(id_user=2002, description='Chamelecón, San Pedro Sula, Cortés, Honduras', coordinate='-88.01631861741664,15.426183566794776'),
        
    ]
    return users_adress