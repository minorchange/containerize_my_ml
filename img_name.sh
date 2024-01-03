get_model_repo_name() {
	# save current directory
	pushd . > /dev/null
	# go to parent repo where the model is located
	cd ..
	model_repo_name=$(basename `git rev-parse --show-toplevel`)
	# go back to saved directory
	popd > /dev/null
	echo $model_repo_name
}

create_img_name() {
	
	local appname_file="../appname.md"
	if [ -e "$appname_file" ]; then
		echo $(cat "$appname_file")
	else
		echo $(get_model_repo_name)
	fi
}

echo $(create_img_name)