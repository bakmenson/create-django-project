# Create a django project and install virtualenv using pyenv or remove project and virtualenv.

## Dependencies
 - [pyenv](https://github.com/pyenv/pyenv)
 - [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv)

## Hot to install:
1. 
    ``` bash
    $ git clone https://github.com/bakmenson/django_project.git ~/.django_project
    ```

2. 
    ``` bash
    $ chmod +x ~/.django_project/django_project
    ```

3. Export PATH
  - For **bash**:
    ``` bash
    $ echo 'export PATH="$PATH:/$HOME/.django_project"' >> ~/.bashrc
    ```
    
  - For **Zsh**:
    ``` zsh
    $ echo 'export PATH="$PATH:/$HOME/.django_project"' >> ~/.zshrc
    ```

4. Restart Terminal

## Hot to use:

- Create Project
    ``` bash
    $ django_project -c
    ```
    
- Delete Project
    ``` bash
    $ cd <directory with project directory>
    $ django_project -d
    ```
