import streamlit as st
from beem import Hive
import json, os
from dotenv import load_dotenv

load_dotenv()

posting_key = os.getenv("POSTING_KEY")

# Conectar a un nodo de Hive
h = Hive(node=["https://api.hive.blog"], keys=[posting_key])

st.markdown("# Publicador de Post")

with st.form("my_form"):

    post_autor = st.text_input("Enter account name")

    post_title = st.text_input("Enter post title")

    post_content = st.text_area("Enter the content of the post")

    post_image = st.file_uploader("Enter the image (Only preview)")

    post_image_url = st.text_input("URL of the image (optional)")

    post_tags = st.text_input("Enter the post tags (separated by commas)")

    submmit_button = st.form_submit_button(label="post", use_container_width=True)

if submmit_button:
    # Vista previa local de imagen subida (no se envia en json)
    if post_image is not None:
        st.image(post_image, caption="Vista previa", use_container_width =False)

    # Normalizar tags a lista
    tags_list = []
    if post_tags:
        parts = [t.strip() for t in post_tags.split(',')]
        for t in parts:
            if not t:
                continue
            t = t.lower().lstrip('#').replace(' ','-')
            if t and t not in tags_list:
                tags_list.append(t)

    # Preparar metadata compatible (solo URLs)
    images_meta = [post_image_url] if post_image_url else []

    # Publicar el post
    post = h.post(
        title=post_title,
        body=post_content,
        author=post_autor,
        json_metadata=json.dumps({"tags": tags_list, "image": images_meta}),
        blockchain_instance=h
    )
    
    # Mostrar un mensaje de confirmacion
    st.success("Post successfully published")

    # Mostrar el enlace del post
    st.write(f"https://peakd.com/@{post_autor}")