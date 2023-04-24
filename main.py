from website import create_app

app = create_app()

if __name__ == '__main__': # only run if this file directly is run
    app.run(debug=True) # auto start when changes made