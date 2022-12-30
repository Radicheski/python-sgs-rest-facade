from app import create_application

if __name__ == '__main__':
    main = create_application()
    main.run(host='0.0.0.0', debug=True)
