#include "ElevensButtonEventHandler.h"
#include <iostream>

ElevensButtonEventHandler::ElevensButtonEventHandler(){}

ElevensButtonEventHandler::ElevensButtonEventHandler(Elevens *setElevens) {
    elevens = setElevens;
}

void ElevensButtonEventHandler::registerButtonManager(ElevensButtonManager *setbtnMgr) {
    btnMgr = setbtnMgr;
}

void ElevensButtonEventHandler::invoke(Button *btn) {    
    Elevens *Game = Game->getInstance();
    if (Game->selected.size() == 1) {
        if (Game->selected[0] == btn){
            return; // Stops you from selecting the same button twice
        }
    }
    Game->selected.push_back(reinterpret_cast<ElevensButton*>(btn));
}