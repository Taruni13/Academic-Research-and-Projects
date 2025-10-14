# Healthcare Appointment Analysis — Streamlit Dashboard

Overview
- Interactive Streamlit dashboard for analyzing patient appointment data and predicting no-shows.
- Uses the provided cleaned CSV (cleaned_dataset.csv). Basic preprocessing script (preprocess.py) is included to regenerate the cleaned CSV from raw dataset.csv.
- Simple RandomForest pipeline persists to `model.joblib` for ad-hoc predictions.

Project structure
- app.py — Streamlit app, UI, filters, plots, train/load model buttons and ad-hoc prediction form.
- analysis.py — Data loading, basic summary stats and plotting helpers used by the app.
- model.py — Feature preparation, training pipeline, evaluation and save/load functions (uses joblib).
- preprocess.py — One-off cleaning pipeline that turns raw `dataset.csv` into `cleaned_dataset.csv`.
- cleaned_dataset.csv — Cleaned data used by the app (already in repo).
- requirements.txt — Python dependencies for the app.
- model.joblib — Saved trained model (created after you train from the app or run model.train_model).

Quickstart (macOS)
1. Open the project folder:
   cd "/Users/ZIVA KEVIN/Documents/dev/Academic Research and Projects/Academic-Research-and-Projects/Healthcare Appointment Analysis"

2. Create and activate a virtual environment (recommended):
   python3 -m venv env
   source env/bin/activate

3. Install dependencies:
   pip install --upgrade pip
   pip install -r requirements.txt

4. (Optional) Regenerate cleaned CSV from raw data:
   python preprocess.py

5. Run the Streamlit app:
   streamlit run app.py

6. In the app:
   - Use sidebar filters to explore the dataset.
   - Click "Train model" to train and save a RandomForest classifier (model.joblib).
   - Click "Load model" to load an existing saved model.
   - Use the ad-hoc prediction form to get probability of no-show for a custom input.

Notes & troubleshooting
- If matplotlib / Streamlit raises a layout/axes error, restart the app. The repo returns explicit Figure objects to Streamlit to avoid global-plt issues.
- If requirements install fails, confirm you are in the correct folder and virtualenv is activated. Use `ls` to verify `requirements.txt` exists.
- Large CSVs: consider converting to parquet for faster loads and smaller repo footprint.
- If the model training fails due to class imbalance, add class_weight="balanced" to the classifier or apply sampling (SMOTE).

Extending the app
- Replace the RandomForest with hyperparameter tuning (GridSearchCV) or different algorithms.
- Add SHAP explainability to show feature impacts (install `shap` and augment model.py).
- Persist dataset in a data folder or cloud storage and load lazily.

License
- MIT — adapt as needed.

Contact / Contributing
- Create a PR with changes;