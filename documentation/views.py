from django.views.generic import TemplateView
import os
import markdown


def load_markdown(template_name):
    path = os.path.join('','doc_files',template_name)
    with open(path,'r',encoding='utf-8') as file:
        md_file = file.read()
    
    rendered_file = markdown.markdown(md_file,extensions=['fenced_code','tables'])

    return rendered_file

class MarkDownRenderView(TemplateView):
    template_name = "docs.html"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        template_name = kwargs.get('file', 'main.md')

        markdown_file = load_markdown(template_name)

        context['markdown_file'] = markdown_file

        return context