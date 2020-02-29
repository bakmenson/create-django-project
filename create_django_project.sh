#!/bin/bash

project_dir=$1
virtual_env=$2
python_version=$3

VIRTUALENV_PATTERN="^(.+)..created.+versions.(.+).$"

is_available_python_version=false
is_available_virtualenv=false

cd ../

if [[ $project_dir == "" ]]; then
	echo "----------------------------------------------------------------"
	echo "You did not specify project dir, virtual env and python version."
	echo "----------------------------------------------------------------"
	exit 1
else
	if [[ -d $project_dir ]]; then
		echo "----------------------------------------------------"
		echo "Directory '"$project_dir"' exists."
		echo "Remove directory '"$project_dir"?'"
		echo "Press 'Enter' or 'y' to delete or any key to exit."
		echo "----------------------------------------------------"

		read -s -n 1 delete

		if [[ $delete == "" || $delete == "y" ]]; then
			rm -rf $project_dir
			echo "Directory removed."
		else
			echo "Exit" && exit 1
		fi
	fi
fi

if [[ $virtual_env != "" ]]; then

	while read -r line; do
		if [[ $line =~ ${VIRTUALENV_PATTERN} ]]; then
			pyenv_version=${BASH_REMATCH[2]}
			if [[ $virtual_env =~ ${BASH_REMATCH[1]} ]]; then
				is_available_virtualenv=true
				echo "-----------------------------------------------------------"
				echo "Virtualenv '"$virtual_env"' already exists ('"$pyenv_version"')."
				echo ""
				echo "Set virtualenv '"$virtual_env"' for project dir with '"$pyenv_version"'?"
				echo "Press 'Enter' or 'y' to continue or any key to exit."
				echo "-----------------------------------------------------------"
			fi
		fi
	done < <(pyenv virtualenvs)

	if $is_available_virtualenv; then
		read -s -n 1 answer

		if [[ $answer == "" || $answer == "y" ]]; then
			mkdir $project_dir && cd $project_dir
			pyenv local $virtual_env
		else
			rm -rf $project_dir
			echo "Exit" && exit 1
		fi
	fi

	if [[ $python_version != "" ]]; then
		while read -r line; do
			if [[ $line == $python_version ]]; then
				is_available_python_version=true
			fi
		done < <(pyenv versions)

		if ! $is_available_python_version; then
			{
				pyenv install $python_version
			} || {
				echo "" && echo "Exit"
				rm -rf $project_dir && exit 1
			}

			is_available_python_version=true
		fi
	fi

	if $is_available_python_version && ! $is_available_virtualenv; then
		pyenv virtualenv $python_version $virtual_env
		mkdir $project_dir && cd $project_dir
		pyenv local $virtual_env
		echo "" && echo "Done"
	fi
else
	echo "---------------------------------------------------"
	echo "You did not specify virtual env and python version."
	echo "---------------------------------------------------"
	exit 1
fi

django_project_name="${project_dir//'-'/$'_'}"

pip install --upgrade pip

{
	pip freeze | grep Django
} || {
	pip install django
}

django-admin startproject $django_project_name

mv $django_project_name/manage.py ./
mv $django_project_name/$django_project_name/* $django_project_name
rm -rf $django_project_name/$django_project_name/

python manage.py migrate
python manage.py createsuperuser
