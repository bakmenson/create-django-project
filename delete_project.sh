#!/bin/bash

project_dir=$1

cd ../

if [[ $project_dir == "" ]]; then
	echo "---------------------------------------------"
	echo "You did not specify project dir for removing."
	echo "---------------------------------------------"
	exit 1
else
	if [[ -d $project_dir ]]; then

		if [[ -e $project_dir/.python-version ]]; then

			read -r env < $project_dir/.python-version

			echo "--------------------------------------------------"
			echo "Uninstall virtualenv '"$env"'?"
			echo "Press 'Enter' or 'y' to delete or any key to exit."
			echo "--------------------------------------------------"

			read -s -n 1 delete_env

			if [[ $delete_env == "" || $delete_env == "y" ]]; then
				pyenv uninstall $env
				echo "Virtualenv '"$env"' uninstalled."
			fi

			rm -rf $project_dir
			echo "Project removed."
			echo "--------------------------------------------------"

		fi

	else
		echo "--------------------------------------------------"
		echo "Directory '"$project_dir"' does not exist."
		echo "--------------------------------------------------"
		exit 1
	fi
fi
