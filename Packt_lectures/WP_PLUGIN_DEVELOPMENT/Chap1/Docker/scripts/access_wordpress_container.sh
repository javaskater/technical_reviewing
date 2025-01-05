#!/usr/bin/env bash

function trace(){
    msg=$1;
    echo "$(date '+%d/%m/%Y %H:%M:%S') - ${msg}";
}

function passing_command_in_the_wp_container(){
    command=$1; #The command string
    docker exec -it docker-wordpress-1 sh -c "$command"
}

function main(){
trace "accesssing the wordpress conntainer";
passing_command_in_the_wp_container "bash";
ret3=$?;
}

# main prog
log_file="./$(basename $0)_$(date '+%d%m%Y_%H%M%S').log";
main 2>&1 | tee $log_file;

