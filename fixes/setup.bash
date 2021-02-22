#!/usr/bin/env bash
# generated from catkin/cmake/templates/setup.bash.in

CATKIN_SHELL=bash

#ei hyvä, toimii kun ei sada
#jos liian pitkä, nollaa export $GAZEBO_MODEL_PATH=""
_WS_LCAL_MODLS=$(builtin cd "`dirname "${BASH_SOURCE[0]}"`" > /dev/null && pwd)
_WS_LCAL_MODLS="$_WS_LCAL_MODLS/../src/samk_robowar_world/models"
export GAZEBO_MODEL_PATH=$_WS_LCAL_MODLS:$GAZEBO_MODEL_PATH

# source setup.sh from same directory as this file
_CATKIN_SETUP_DIR=$(builtin cd "`dirname "${BASH_SOURCE[0]}"`" > /dev/null && p>
. "$_CATKIN_SETUP_DIR/setup.sh"
