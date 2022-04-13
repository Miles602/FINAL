from models import db, Users,Posts

class UserRepository:

    #Grabs user id
    def get_user_by_id(self, users_id):
        id = Users.query.get_or_404(users_id)

        return id

    def get_all_users(self):
        getAll = Users.query.all()

        return getAll

    #Creates a new user and saves it to the database
    def create_user(self, username, passcode):
        new_user = Users(username = username, passcode = passcode)

        db.session.add(new_user)
        db.session.commit()

        return new_user

    #Determines if user is an existing user
    def login(self, temp_username, temp_passcode):
        confirmed_user = Users.query.filter_by(username = temp_username, passcode = temp_passcode).first()

        if confirmed_user.username == temp_username and confirmed_user.passcode == temp_passcode:
            is_user = True
        else:
            is_user = False

        return is_user


    def search_post(self, title):
        title_search=title
        match=Posts.query.filter(Posts.post_title.like("%"+title_search+"%")).all()

        return match

    def create_post(self,post_title,post_comment):
        new_post= Posts(post_title=post_title,post_comment=post_comment)
        db.session.add(new_post)
        db.session.commit()
        return new_post

    def get_post_by_id(self,post_id):
        single_post= Posts.query.get_or_404(post_id)
        return single_post


    def get_all_posts(self):
        all_posts= Posts.query.all()
        return all_posts

user_repository_singleton = UserRepository()
