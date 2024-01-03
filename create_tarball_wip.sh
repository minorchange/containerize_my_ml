#!/bin/bash


# Source the .env file
# if [[ -f ../.env ]]; then
#     source ../.env
# else
#     echo "Error: .env file not found"
#     exit 1
# fi


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

# Example of usage:
version=$(get_git_commit_hash)-$(date +%Y%m%d%H%M%S)
echo "Git Commit Hash: $version"

# create_tarball $ZSC_IMG_NAME $ZSC_VERSION ../path_to_containerize_paren_folder cleanup