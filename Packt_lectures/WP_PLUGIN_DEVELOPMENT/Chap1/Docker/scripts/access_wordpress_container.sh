#!/usr/bin/env bash

function trace(){
    msg=$1;
    echo "$(date '+%d/%m/%Y %H:%M:%S') - ${msg}";
}

function passing_command_in_the_wp_container(){
    command=$1; #The command string
    docker exec -it docker-wordpress-1 sh -c "$command"
}

function logging_wordpress_in_container(){
    docker logs docker-wordpress-1 1>/dev/null
}

function main(){
    if [ -z "$1" ]
    then
        trace "accesssing the wordpress conntainer";
        passing_command_in_the_wp_container "bash";
        ret3=$?;
    elif [[ "$1" == "log" ]]
    then
        trace "getting the wordpress logs from the container"
        logging_wordpress_in_container
    else
        trace "the ${1} paramter if exists must be log"
    fi
}

# main prog
log_file="./$(basename $0)_$(date '+%d%m%Y_%H%M%S').log";
main $1 2>&1 | tee $log_file;

