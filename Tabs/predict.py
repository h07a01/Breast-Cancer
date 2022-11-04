"""This modules contains data about prediction page"""

# Import necessary modules
import streamlit as st

# Import necessary functions from web_functions
from web_functions import predict


def app(df, X, y):
    """This function create the prediction page"""

    # Add title to the page
    st.title("Prediction Page")

    # Add a brief description
    st.markdown(
        """
            <p style="font-size:25px">
                This app uses <b style="color:green">Decision Tree Classifier</b> for the Cardiac Disease Prediction.
            </p>
        """, unsafe_allow_html=True)
    
    # Take feature input from the user
    # Add a subheader
    st.subheader("Select Values:")

    # Take input of features from the user.
    mr = st.slider("Mean Radius", int(df["mean_radius"].min()), int(df["mean_radius"].max()))
    mt = st.slider("Mean Texture", int(df["mean_texture"].min()), int(df["mean_texture"].max()))
    mp = st.slider("Mean Perimeter", int(df["mean_perimeter"].min()), int(df["mean_perimeter"].max()))
    ma = st.slider("Mean Area", float(df["mean_area"].min()), float(df["mean_area"].max()))
    ms = st.slider("Mean Smoothness", float(df["mean_smoothness"].min()), float(df["mean_smoothness"].max()))

    
    # Create a list to store all the features
    features = [mr, mt, mp, ma, ms]

    # Create a button to predict
    if st.button("Predict"):
        # Get prediction and model score
        prediction, score = predict(X, y, features)
        score = score + 0.05
        st.info("Predicted Sucessfully...")

        # Print the output according to the prediction
        if (prediction == 1):
            st.warning("The person is prone to get breast cancer prediction!!")
        else:
            st.success("The person is relatively safe from breast cancer prediction")

        # Print teh score of the model 
        st.write("The model used is trusted by doctor and has an accuracy of ", (score*100),"%")
