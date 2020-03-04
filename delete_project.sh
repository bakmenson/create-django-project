#!/bin/bash

project_dir=$1

separator() { printf %$1s | tr " " "-" && echo ""; }

message() { separator $2 && echo -e $1 && separator $2; }

cd ../

if [[ $project_dir == "" ]]; then
	message "You did not specify project dir for removing." 45
	exit 1
else
	if [[ -d $project_dir ]]; then

		if [[ -e $project_dir/.python-version ]]; then

			read -r env < $project_dir/.python-version

			message "Uninstall virtualenv '"$env"'?\nPress 'Enter' \
				or 'y' to delete or any key to exit." 50

			read -s -n 1 delete_env

			if [[ $delete_env == "" || $delete_env == "y" ]]; then
				pyenv uninstall $env
				echo "Virtualenv '"$env"' uninstalled."
			fi
		fi

		rm -rf $project_dir
		message "Project removed." 20

	else
		message "Directory '"$project_dir"' does not exist." 50
		exit 1
	fi
fi
