#!/bin/bash

separator() { printf %$1s | tr " " "-" && echo ""; }

echo_message() { separator $2 && echo -e $1 && separator $2; }

action=$1

if [[ $action == "-c" ]]; then

	echo_message "Input project dir." 30 && read create_dir
	echo_message "Input virtua env." 30 && read virtual_env
	echo_message "Input Python version." 30 && read python_version

	chmod +x create_project.sh

	./create_project.sh $create_dir $virtual_env $python_version

elif [[ $action == "-d" ]]; then

	echo_message "Input project dir." 30 && read remove_project_dir

	chmod +x delete_project.sh

	./delete_project.sh $remove_project_dir

else
	echo_message "Wrong command." 20 && exit 1
fi
