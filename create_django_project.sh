#!/bin/bash

#project_dir=$1
virtual_env=$1
python_version=$2

VIRTUAL_ENV_PATTERN="^[a-z-]+"

is_available_python_version=false
is_available_virtual_env=false

if [[ $python_version != "" ]]; then
	while read -r line; do
		if [[ $line == $python_version ]]; then
			is_available_python_version=true
		fi
	done < <(pyenv versions)

	if ! $is_available_python_version; then
		pyenv install $python_version
		is_available_python_version=true
	fi
fi

#cd ../

#if [[ -d $project_dir ]]; then
#	rm -rf $project_dir
#fi

#mkdir $project_dir
#cd $project_dir

if [[ $virtual_env != "" ]]; then
	is_available_virtual_env=true
	while read -r line; do
		if [[ $line =~ ${VIRTUAL_ENV_PATTERN} ]]; then
			if [[ $virtual_env =~ ${BASH_REMATCH} ]]; then
				#pyenv local $virtual_env
				#exit 0
				echo $virtual_env
			fi
		fi
	done < <(pyenv virtualenvs)
fi

if $is_available_python_version && $is_available_virtual_env; then
	echo $is_available_python_version
	echo $is_available_virtual_env
	#pyenv virtualenv $python_version $virtual_env
fi
