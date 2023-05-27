import gradio as gr
import trainmodel

index = trainmodel.construct_index("docs")
trainmodel.iface.launch(share=True)