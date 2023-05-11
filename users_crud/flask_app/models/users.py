from flask_app.config.mysqlconnection import connectToMySQL

class User :
    DB = 'users_schema'
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def add_user(cLs, data):
        query = """
        INSERT INTO users (first_name, last_name, email)
        VALUES (%(first_name)s, %(last_name)s, %(email)s);
        """
        result = connectToMySQL(cLs.DB).query_db(query, data)
        return result


    @classmethod 
    def get_all_users(cLs):
        query = """
        SELECT * FROM users;
        """

        result = connectToMySQL(cLs.DB).query_db(query)
        #print(result)

        all_users = []
        for user in result:
            all_users.append(cLs(user))
        return all_users


    @classmethod
    def get_one_user(cLs,data):
        query = """
        SELECT * FROM users
        WHERE id = %(id)s;
        """
    
        result = connectToMySQL(cLs.DB).query_db(query, data)
        return cLs(result[0])


    @classmethod
    def update_user(cLs, data):
        query = """
        UPDATE users
        SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s
        WHERE id = %(id)s;
        """

        result = connectToMySQL(cLs.DB).query_db(query, data)
        return result


    @classmethod
    def delete_user(cLs, data):
        query = """
        DELETE FROM users
        WHERE id = %(id)s;
        """

        result = connectToMySQL(cLs.DB).query_db(query, data)
        return result