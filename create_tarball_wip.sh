#!/bin/bash


# Source the .env file
# if [[ -f ../.env ]]; then
#     source ../.env
# else
#     echo "Error: .env file not found"
#     exit 1
# fi




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

create_version() {
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

create_image_name() {
    
    local appname_file="../appname.md"
    if [ -e "$appname_file" ]; then
        echo $(cat "$appname_file")
    else
        echo $(get_model_repo_name)
    fi
}


create_tarball(){
    
    img_name=$1
    img_tag=$2
    containerize_my_ml_parent_foler=$3
    cleanup_image_afterwards=$4
    
    img_reference="$img_name":"$img_tag"
    current_path=$(pwd)
    
    echo "----> "Building "$img_reference"
    cd $containerize_my_ml_parent_foler
    docker build -f containerize_my_ml/Dockerfile -t $img_reference .

    tar_path="$img_name"_"$img_tag".tar.gz
    echo "----> "Writing img tarballl "$tar_path"
    cd $current_path
    docker save $img_reference > $tar_path

    docker_id=$(docker images "$img_reference" -a -q)
    if [[ "$cleanup_image_afterwards" == "cleanup" ]]
    then
        echo "----> "Remove image with name: "$img_reference" and id: "$docker_id"
        docker rmi $docker_id
    else
        echo "----> "Not removing the image "$img_reference" with id: "$docker_id"
    fi
}

create_tarball $(create_image_name) $(create_version) ../ cleanup