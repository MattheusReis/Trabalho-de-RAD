from settings.flask_aap import create_app

app = create_app()


if __name__ == '__main__':
    app.run(port=5050, debug=True)
    