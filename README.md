# Adobe Take Home Assignment


Contents of the directory:
- Reports
    - Data_Analysis_Report.pdf
    - Recommender_System_ML_Design.pdf
    - Community_Recommendation_Engine_Experiment.pdf
    - Business_Evaluation_Report.pdf
- Modeling Artifacts
    - Data Analysis.ipynb
    - ModelTraining.ipynb
    - save_artifacts with saved model file, checkopoints, tensorboard logs and other artifacts.
    - data directory
- Docker Deployment
    - streamlit_app.py
    - requirement.txt
    - Dockerfile

To run the app
- cd to this directory
- Build docker image by running
     `docker build -t recommendation .`
- Run streamlit app by running
    `docker run -p 8501:8501 recommendation`
- Navigate to the URL display.
- On the app, enter any user id and see the recommendations.



