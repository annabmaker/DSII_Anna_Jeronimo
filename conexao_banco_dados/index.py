import mysql.connector
from mysql.connector import Error

def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("Conexão com o MySQL bem-sucedida!")
    except Error as e:
        print(f"O erro '{e}' ocorreu")
    return connection

def execute_query(connection, query, params=None):
    cursor = connection.cursor()
    try:
        cursor.execute(query, params or ())
        connection.commit()
        print("Query executada com sucesso")
    except Error as e:
        print(f"O erro '{e}' ocorreu ao executar a query")

def execute_read_query(connection, query, params=None):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query, params or ())
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"O erro '{e}' ocorreu ao executar a query de leitura")
    return result

if __name__ == '__main__':
    meu_banco = "senaidb"
    conn = create_connection("localhost", "root", "senai", meu_banco)

    if conn is not None and conn.is_connected():
        try:
            insert_vendedor_query = "INSERT INTO Vendedores (Nome) VALUES (%s)"
            execute_query(conn, insert_vendedor_query, ("João Silva",))
            execute_query(conn, insert_vendedor_query, ("Maria Oliveira",))

            select_vendedores_query = "SELECT IDVendedor, Nome FROM Vendedores"
            vendedores = execute_read_query(conn, select_vendedores_query)

            if vendedores:
                print("\nVendedores cadastrados:")
                for vendedor in vendedores:
                    print(vendedor)

            data_venda_str = "01/01/2016"
            insert_venda_query_com_str_to_date = """
            INSERT INTO Vendas (IDVendedor, IDCliente, Data, Total)
            VALUES (%s, %s, STR_TO_DATE(%s, '%d/%m/%Y'), %s)
            """
            execute_query(conn, insert_venda_query_com_str_to_date, (1, 1, data_venda_str, 8053.60))
        finally:
            if conn.is_connected():
                conn.close()
                print("Conexão com o MySQL fechada.")
    else:
        print("Não foi possível conectar ao banco de dados.")
