import connexion

if __name__ == '__main__':
    app = connexion.FlaskApp(__name__)
    app.add_api('swagger.yml')
    app.run(host='0.0.0.0', port=5000, debug=True)