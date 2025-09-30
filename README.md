# 📚 Docs App for Django

Many developers prefer writing documentation in Markdown—it's simple, readable, and version-control friendly. This Django app makes it easy to render Markdown-based documentation directly in your project.

The concept is straightforward: organize your documentation inside a dedicated folder and let the app handle the rendering.



Place your Markdown files inside the doc_files directory and watch the magic happen ✨

## 🚀 Getting Started

Follow these steps to integrate the Docs App into your Django project:
1. Install the app

Clone this repository and copy the documentation app into your Django project. 
Then, install the following dependencies:
*   Markdown
*   Pygments
```python
pip install markdown
```
```python
pip install Pygments
```
Then, add it to your INSTALLED_APPS in settings.py:
```
INSTALLED_APPS = [
    ...
    "documentation",
    ...
]
```

2. Create your documentation folder

Inside your project, create a folder named doc_files and add a file called main.md. This will serve as the homepage of your documentation.

3. Configure your URLs

In your project's urls.py, include the app's URL patterns:
from django.urls import path, include

```
urlpatterns = [
    ...
    path("docs/", include("documentation.urls")),
    ...
]
```

Now it will render your main.md file. You can add more Markdown files and subdirectories as needed.
```
python manage.py runserver
```
Then go to the **docs/** url.

And that's it! You're ready to build clean, navigable documentation using nothing but Markdown and Django.

# Future features

Now I'm trying to make this plugin an installable package

```python
pip install django-documents
```
