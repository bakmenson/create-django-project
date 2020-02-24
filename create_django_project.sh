#!/bin/bash

project_dir=$1
virtual_env=$2
python_version=$3

VIRTUAL_ENV_PATTERN="^[a-z-]+"

#PYTHON_VERSION_PATTERN="^..\d.\d.\d$"
PYTHON_VERSION_PATTERN="^\w.\w.\w$"

cd ../

if [[ -d $project_dir ]]; then
	rm -rf $project_dir
fi

mkdir $project_dir
cd $project_dir

while read -r line; do
	if [[ $line =~ ${VIRTUAL_ENV_PATTERN} ]]; then
		if [[ $virtual_env =~ ${BASH_REMATCH} ]]; then
			pyenv local $virtual_env
		fi
	fi
done < <(pyenv virtualenvs)

while read -r line; do
	if [[ $line =~ ${PYTHON_VERSION_PATTERN} ]]; then
		if [[ $python_version =~ ${BASH_REMATCH} ]]; then
			echo $python_version
		fi
	fi
done < <(pyenv versions)
