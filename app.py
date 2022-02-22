import gradio as gr
from creator import PullJob
import os
import glob


def job_report(url, file, nouns, verbs):
    if len(glob.glob(f'{os.getcwd()}/report/*')) >= 1:
        for f in glob.glob(f'{os.getcwd()}/report/*'):
            if f != f'{os.getcwd()}/report/.gitkeep':
                os.remove(f)

    pull = PullJob(url, file, nouns, verbs)
    pull.run_all()

    return 'report/'+str(file)+'.pdf'
    
gr.Interface(job_report, inputs=["text", "text", gr.inputs.Radio([10, 15, 20]), gr.inputs.Radio([10, 15, 20])], 
             outputs="file", 
             title="Job Report Creator",
             description="This app will parse a Linkedin job and generate a report based on the most frequent nouns and verbs").launch()