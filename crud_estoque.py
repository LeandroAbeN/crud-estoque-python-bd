import psycopg2

# Configurações do banco
DB_HOST = "localhost"
DB_NAME = "crud_estoque"
DB_USER = "postgres"
DB_PASS = "1"
DB_PORT = "5432"

# Função para abrir conexão
def abrir_conexao():
    return psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS,
        port=DB_PORT
    )

# -----------------------------
# CRUD
# -----------------------------
def selecionar():
    try:
        conn = abrir_conexao()
        cur = conn.cursor()
        cur.execute("SELECT * FROM estoque ORDER BY codigo;")
        registros = cur.fetchall()
        print("\n--- Lista de Produtos ---")
        for r in registros:
            print(f"Código: {r[0]} | Nome: {r[1]} | Marca: {r[2]} | Valor: R$ {r[3]}")
        cur.close()
        conn.close()
    except Exception as e:
        print("Erro ao selecionar:", e)

def inserir(codigo, nome, marca, valor):
    try:
        conn = abrir_conexao()
        cur = conn.cursor()
        cur.execute("INSERT INTO estoque (codigo, nome, marca, valor) VALUES (%s, %s, %s, %s);",
                    (codigo, nome, marca, valor))
        conn.commit()
        print("✅ Produto inserido com sucesso!")
        cur.close()
        conn.close()
    except Exception as e:
        print("Erro ao inserir:", e)

def atualizar(codigo, nome, marca, valor):
    try:
        conn = abrir_conexao()
        cur = conn.cursor()
        cur.execute("UPDATE estoque SET nome=%s, marca=%s, valor=%s WHERE codigo=%s;",
                    (nome, marca, valor, codigo))
        conn.commit()
        print("✅ Produto atualizado com sucesso!")
        cur.close()
        conn.close()
    except Exception as e:
        print("Erro ao atualizar:", e)

def excluir(codigo):
    try:
        conn = abrir_conexao()
        cur = conn.cursor()
        cur.execute("DELETE FROM estoque WHERE codigo=%s;", (codigo,))
        conn.commit()
        print("✅ Produto excluído com sucesso!")
        cur.close()
        conn.close()
    except Exception as e:
        print("Erro ao excluir:", e)

# -----------------------------
# Menu interativo
# -----------------------------
def menu():
    while True:
        print("\n=== CRUD Estoque ===")
        print("1 - Listar produtos")
        print("2 - Inserir produto")
        print("3 - Atualizar produto")
        print("4 - Excluir produto")
        print("0 - Sair")
        op = input("Escolha: ")

        if op == "1":
            selecionar()
        elif op == "2":
            codigo = int(input("Código: "))
            nome = input("Nome: ")
            marca = input("Marca: ")
            valor = float(input("Valor: "))
            inserir(codigo, nome, marca, valor)
        elif op == "3":
            codigo = int(input("Código do produto a atualizar: "))
            nome = input("Novo Nome: ")
            marca = input("Nova Marca: ")
            valor = float(input("Novo Valor: "))
            atualizar(codigo, nome, marca, valor)
        elif op == "4":
            codigo = int(input("Código do produto a excluir: "))
            excluir(codigo)
        elif op == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()
