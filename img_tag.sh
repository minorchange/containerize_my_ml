get_git_commit_hash() {
	local commit_hash
	commit_hash=$(git log -1 --pretty=format:"%h" 2>/dev/null)
	
	if [ -n "$commit_hash" ]; then
		echo "$commit_hash"
		return 1
	else
		return "x"
	fi
}

get_current_git_tag() {
	# Set the script to exit on error
	if git describe --tags --exact-match HEAD >/dev/null 2>&1; then
		current_tag=$(git describe --tags 2>/dev/null)
		if [ -n "$current_tag" ]; then
			echo "$current_tag"
		else
			echo "X"
		fi
	else
		echo "x"
	fi
}

create_img_tag() {
	containerize_repo_hash=$(get_git_commit_hash)
	# save current directory
	pushd . > /dev/null
	# go to parent repo where the model is located
	cd ..
	model_repo_hash=$(get_git_commit_hash)
	model_repo_tag=$(get_current_git_tag)
	date=$(date +%y%m%d)
	version=$model_repo_tag-$model_repo_hash-$containerize_repo_hash-$date
	# go back to saved directory
	popd > /dev/null
	echo $version
}

echo $(create_img_tag)