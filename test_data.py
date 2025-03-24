from database import get_connection

def test_data_insertion():
    connection = get_connection()
    if connection:
        try:
            cursor = connection.cursor()
            
            # Insert test user
            insert_user = """
            INSERT INTO users (username, email, password, is_admin)
            VALUES (%s, %s, %s, %s)
            """
            user_data = ("test_user", "test@example.com", "test123", False)
            cursor.execute(insert_user, user_data)
            
            # Insert test scrap item
            insert_scrap = """
            INSERT INTO scrap_items (name, type, weight, price, user_id)
            VALUES (%s, %s, %s, %s, %s)
            """
            scrap_data = ("Test Metal", "Steel", 10.5, 525.0, cursor.lastrowid)
            cursor.execute(insert_scrap, scrap_data)
            
            # Commit the changes
            connection.commit()
            print("Test data inserted successfully!")

            # Verify the data
            print("\nVerifying inserted data:")
            cursor.execute("SELECT * FROM users")
            print("\nUsers:")
            for row in cursor.fetchall():
                print(row)

            cursor.execute("SELECT * FROM scrap_items")
            print("\nScrap Items:")
            for row in cursor.fetchall():
                print(row)

        except Exception as e:
            print(f"Error: {e}")
            connection.rollback()
        finally:
            cursor.close()
            connection.close()
            print("\nConnection closed.")

if __name__ == "__main__":
    test_data_insertion()