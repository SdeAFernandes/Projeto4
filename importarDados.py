import csv
import sqlite3
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "db.sqlite3"
CSV_PATH = BASE_DIR / "base_filmes.csv"


def importar_dados():
    conn = sqlite3.connect(DB_PATH)
    try:
        with conn:
            with CSV_PATH.open(newline="", encoding="utf-8") as csvfile:
                for linha in csv.DictReader(csvfile):
                    nome_genero = linha["genero"].strip()
                    resultado = conn.execute(
                        "SELECT id FROM filmes_generos WHERE nome = ?",
                        (nome_genero,),
                    ).fetchone()

                    if resultado:
                        genero_id = resultado[0]
                    else:
                        cursor = conn.execute(
                            "INSERT INTO filmes_generos (nome) VALUES (?)",
                            (nome_genero,),
                        )
                        genero_id = cursor.lastrowid

                    conn.execute(
                        """
                        INSERT INTO filmes_filmes
                            (titulo, descricao, ano_lancamento, genero_id, duracao)
                        VALUES (?, ?, ?, ?, ?)
                        """,
                        (
                            linha["titulo"].strip(),
                            linha["descricao"].strip(),
                            int(linha["ano"]),
                            genero_id,
                            int(linha["duracao"]),
                        ),
                    )
    finally:
        conn.close()

    print("Importação de filmes concluída com sucesso!")


if __name__ == "__main__":
    importar_dados()
