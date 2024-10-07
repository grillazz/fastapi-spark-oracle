import asyncio
import oracledb


async def main():
    async with oracledb.connect_async(user="grillazz", password="oracle",
                                      dsn="localhost/pdbfastapi") as connection:
        print(f"Connected to Oracle Database: {connection.dsn}")
        with connection.cursor() as cursor:
            print(f"Executing SQL statement: {cursor.statement}")
            await cursor.execute("select * from console")
            async for result in cursor:
                print(f"Executing SQL statement: {cursor.statement}")
                print(result)

if __name__ == '__main__':
    asyncio.run(main())
