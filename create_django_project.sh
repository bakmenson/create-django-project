#!/bin/bash

project_dir=$1
virtual_env=$2
python_version=$3

PATTERN="^[a-z-]+"

if [[ -d $project_dir ]]; then
	rm -rf $project_dir
fi

mkdir $project_dir
cd $project_dir

while read -r line; do
	if [[ $line =~ ${PATTERN} ]]; then

		if [[ $virtual_env =~ ${BASH_REMATCH} ]]; then
			pyenv local $virtual_env
		fi

	fi
done < <(pyenv virtualenvs)
