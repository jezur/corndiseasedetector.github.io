# Streamlit API# ----------------------------------------------------------------------------import osfrom PIL import Imageimport streamlit as stfrom cddimgprocess import predict_nocuda, load_model_nocudaimport pandas as pdst.title('Corn Disease Detector (CDD)')st.write(    '''    ## Deep Learning API    Welcome to the CDD API. Here you can predict wether the leaf of a maize    plant is healthy or if it has the `common rust` or the `northern blight`.     '''    )img_data = st.file_uploader(label='Load an image for recognition.',                            type=['png', 'jpg', 'jpeg'])model, optimizer = load_model_nocuda('resnet50-transfer-4.pth')if img_data is not None:    uploaded_img = Image.open(img_data)                     # load image object    st.image(uploaded_img)                                      # display image    img_path = os.path.abspath(img_data.name)                  # get image path    # st.write(img_path)    top_p, top_classes = predict_nocuda(img_path, model)      # make prediction    df = pd.DataFrame([[top_classes[0], top_p[0]],                       [top_classes[1], top_p[1]],                       [top_classes[2], top_p[2]]],                      )    df.columns =['Clase', 'Probabilidad']    st.write(df)    