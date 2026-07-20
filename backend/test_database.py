from database.connection import engine

try:

    connection = engine.connect()

    print("\n✅ PostgreSQL Connected Successfully\n")

    connection.close()

except Exception as e:

    print(e)