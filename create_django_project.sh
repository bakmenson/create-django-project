#!/bin/bash

project_dir=$1
virtual_env=$2
python_version=$3

VIRTUALENV_PATTERN="^(.+)..created.+versions.(.+).$"

is_available_python_version=false
is_available_virtualenv=false

#cd ../
#
#if [[ -d $project_dir ]]; then
#	rm -rf $project_dir
#fi
#
#mkdir $project_dir
#cd $project_dir

if [[ $virtual_env != "" ]]; then

	while read -r line; do
		if [[ $line =~ ${VIRTUALENV_PATTERN} ]]; then
			if [[ $virtual_env =~ ${BASH_REMATCH[1]} ]]; then
				#pyenv local $virtual_env || exit 1
				#exit 0
				echo ""
				echo "Virtualenv" "'"$virtual_env"'" "is exists."
			fi
		fi
	done < <(pyenv virtualenvs)

	if [[ $python_version != "" ]]; then
		while read -r line; do
			if [[ $line == $python_version ]]; then
				is_available_python_version=true
			fi
		done < <(pyenv versions)

		if ! $is_available_python_version; then
			#{
			#	pyenv install $python_version
			#} || {
			#	rm -rf $project_dir && exit 1
			#}

			is_available_python_version=true
		fi
	fi

	if $is_available_python_version && ! $is_available_virtualenv; then
		#pyenv virtualenv $python_version $virtual_env || exit 1
		echo ""
	fi

fi
