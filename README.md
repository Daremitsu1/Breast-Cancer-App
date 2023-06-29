# Breast-Cancer-App

### Steps:
## API reference:
This API provides a prediction for the diagnosis of breast cancer based on input features. It uses a machine learning model trained on breast cancer data.

### Usage:
1. Run the Flask server:
```
python api.py
```
2. Open your web browser and go to http://localhost:8000/apidocs to access the Swagger UI for the API documentation.
3. Use the provided input fields to enter the required parameters for breast cancer diagnosis prediction.
4. Click on the "Try it out!" button to submit the request and view the predicted diagnosis.

### API Endpoints
GET /predict: Predicts the diagnosis of breast cancer based on query parameters.

### API Documentation
The API documentation is available in the Swagger UI. You can access it by running the API server and visiting http://localhost:8000/apidocs in your web browser.
The documentation provides detailed information about the API endpoints, parameters, and responses.
![image](https://github.com/Daremitsu1/Breast-Cancer-App/assets/54842807/0a46ea44-fedf-496b-8caf-19ce5446f068)

## Application Frontend:
This is a Streamlit app for breast cancer classification.

### How to Run

Follow these steps to run the app using Docker:

1. Build the Docker image:
   ```
   docker build -t breast-cancer-app .
2. Run a container based on the image:
    ```
    docker run -p 8501:8501 breast-cancer-app
After executing the above commands, you can access the app at http://localhost:8501.

### Streamlit App Interface:
![image](https://github.com/Daremitsu1/Breast-Cancer-App/assets/54842807/5f31964e-ae67-4664-aaf9-51edc12e9db3)
