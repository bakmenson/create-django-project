# Create a django project and install virtualenv using pyenv or remove project and virtualenv.

### Hot to install:
1. 
    ~~~ bash
    $ git clone https://github.com/bakmenson/django_project.git ~/.django_project
    ~~~

2. 
    ~~~ bash
    $ chmod +x ~/.django_project/django_project
    ~~~

3. Export PATH
  - For **bash**:
    ~~~ bash
    $ echo 'export DP_ROOT="$HOME/.django_project"' >> ~/.bashrc
    $ echo 'export PATH="$PATH:/$HOME/.django_project"' >> ~/.bashrc
    ~~~
    
  - For **Zsh**:
    ~~~ zsh
    $ echo 'export DP_ROOT="$HOME/.django_project"' >> ~/.zshrc
    $ echo 'export PATH="$PATH:/$HOME/.django_project"' >> ~/.zshrc
    ~~~

4. Restart Terminal

### Hot to use:

- Create Project
    ~~~ bash
    $ django_project -c
    ~~~
    
- Delete Project
    ~~~ bash
    $ django_project -d
    ~~~
