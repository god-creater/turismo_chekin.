from flask import Flask, request, jsonify, render_template
import mysql.connector

app = Flask(__name__)

# Configuração da conexão com o banco de dados MySQL
db_config = {
    'host': 'localhost',
    'user': 'root',       # usuário do MySQL
    'password': '',       # senha do MySQL
    'database': 'chekin_db'
}

# Rota para renderizar o HTML
@app.route('/')
def index():
    return render_template('index.html')

# Rota para receber o check-in
@app.route('/checkin', methods=['POST'])
def checkin():
    data = request.get_json()

    # Conexão com o banco de dados
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    # Inserção de dados na tabela
    query = """
    INSERT INTO checkin (first_name, last_name, city, email, phone)
    VALUES (%s, %s, %s, %s, %s)
    """
    values = (data['first_name'], data['last_name'], data['city'], data['email'], data['phone'])

    cursor.execute(query, values)
    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({"message": "Check-in realizado com sucesso!"})

if __name__ == "__main__":
    app.run(debug=True)
