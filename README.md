

# Django Crowd Monitoring Project

This is a Django-based web application for monitoring crowds. It includes a variety of features such as a monitoring panel for detecting crowd activity, a contact page for users to reach out with any problems, a login/signup system, and a homepage.

## Features

- **Monitoring Panel**: 
  - Detects crowd activity and displays an alert when crowd thresholds are met.
  - The page is accessible from the navigation bar and automatically updates with alerts.
  
- **Contact Us Page**: 
  - Users can report issues or problems via a simple contact form.
  
- **Login/Signup System**: 
  - Secure user authentication system for logging in and signing up.
  
- **Home Page**: 
  - Landing page with basic information and navigation options.

- **Events CRUD**: 
  - Users can create, read, update, and delete events. This functionality is available under the Events section of the app.
  - The Event page is integrated with the Monitoring Panel. When users click on "Monitor", they are redirected to the monitoring panel for crowd detection.

## Technologies Used

- Python 3.x
- Django 4.x
- SQLite (default database, can be replaced by PostgreSQL or MySQL)
- HTML, CSS (for front-end design)
- JavaScript (for dynamic updates and alerts)

## Apps in the Project

The project is divided into three Django apps:

1. **base**:
   - Contains the homepage, navigation bar, and other shared components used across the project.
  
2. **monitor**:
   - Manages the monitoring panel for detecting crowd activity.
   - The monitoring panel is displayed here, and alerts are shown when crowd thresholds are detected.

3. **events**:
   - Handles event creation, viewing, updating, and deletion (CRUD functionality).
   - When users click the "Monitor" button in the Events page, they are redirected to the `monitor` app's monitoring panel.

## Prerequisites

Before running the project, make sure you have the following installed:

- Python 3.x
- pip (Python package installer)
- Django 4.x

## Installation

Follow the steps below to set up and run the project on your local machine.

1. **Clone the repository**:

    ```bash
    git clone https://github.com/YagnaSuthar/cmCRUD.git
    cd cmCRUD
    ```

2. **Create a virtual environment** (recommended for managing dependencies):

    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment**:

    - For Windows:

      ```bash
      venv\Scripts\activate
      ```

    - For macOS/Linux:

      ```bash
      source venv/bin/activate
      ```

4. **Install the required dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

    If the `requirements.txt` file is not present, you can manually install the required packages:

    ```bash
    pip install django
    ```

    Additionally, install any other dependencies required for crowd detection if applicable (like OpenCV, TensorFlow, etc.).

5. **Set up the database**:

    Run migrations to set up the database tables:

    ```bash
    python manage.py migrate
    ```

6. **Create a superuser** (for accessing the admin panel):

    ```bash
    python manage.py createsuperuser
    ```

    Follow the prompts to create a superuser account.

7. **Run the server**:

    Start the Django development server:

    ```bash
    python manage.py runserver
    ```

    This will start the project at `http://127.0.0.1:8000/`. You can access the application by opening this URL in your web browser.

## Usage

- **Monitoring Panel**: 
  - Access this feature from the navigation bar. The panel will display an alert whenever crowd activity is detected.
  
- **Login/Signup**: 
  - You can register as a new user or log in with your existing credentials. Upon successful login, you’ll be directed to the home page.

- **Events CRUD**: 
  - Go to the Events page to create, view, update, or delete events.
  - From the Events page, click on the "Monitor" button to be redirected to the monitoring panel for crowd detection.

- **Contact Us**: 
  - If you have any issues or need assistance, you can use the "Contact Us" form to send a message.

## Folder Structure

- `cmCRUD/`: Main project folder containing settings and configurations.
- `base/`: Django app for the homepage, navigation, and shared components.
- `monitor/`: Django app for monitoring crowd activity and displaying alerts.
- `events/`: Django app for managing events with CRUD functionality.
- `templates/`: Folder for HTML templates.
- `static/`: Static files (CSS, JavaScript, images, etc.)
- `requirements.txt`: Lists the dependencies required to run the project.
  
## Contributing

If you would like to contribute to the project:

1. Fork the repository
2. Create a new branch (`git checkout -b feature-name`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature-name`)
6. Create a new Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Django for building a robust framework
- OpenCV or any other libraries used for crowd detection
- Inspiration from various web applications and tutorials
