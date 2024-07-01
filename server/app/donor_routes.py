from flask import request, jsonify
from . import app, mysql

@app.route('/api/donor/add', methods=['POST'])
def add_donor():
    try:
        data = request.get_json()
        name = data.get('name')
        phone = data.get('phone')
        blood_group = data.get('bloodGroup')
        email=data.get('email')

        cur = mysql.cursor()
        cur.execute("INSERT INTO donor (name, phone, blood_group,email) VALUES (%s ,%s, %s, %s)", (name, phone, blood_group,email))
        mysql.commit()
        cur.close()

        return jsonify({'message': 'Donor added successfully'}), 200
    except Exception as e:
        print(f"Error adding donor: {e}")
        return jsonify({'error': 'Internal Server Error'}), 500