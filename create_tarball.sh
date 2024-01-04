#!/bin/bash


create_tarball(){
    
    img_name=$1
    img_tag=$2
    cleanup_image_afterwards=$3
    
    img_reference="$img_name":"$img_tag"
    containerize_my_ml_path=$(pwd)
    
    echo "----> "Building "$img_reference"
    cd ..
    docker build -f containerize_my_ml/Dockerfile -t $img_reference .
    
    echo "----> "Writing img tarballl "$tar_path"
    tar_path="$img_name"_"$img_tag".tar.gz
    docker save $img_reference > $tar_path

    docker_id=$(docker images "$img_reference" -a -q)
    if [[ "$cleanup_image_afterwards" == "cleanup" ]]
    then
        echo "----> "Remove image with name: "$img_reference" and id: "$docker_id"
        docker rmi $docker_id
    else
        echo "----> "Not removing the image "$img_reference" with id: "$docker_id"
    fi
    cd $containerize_my_ml_path
}

create_tarball $(bash img_name.sh) $(bash img_tag.sh) cleanup