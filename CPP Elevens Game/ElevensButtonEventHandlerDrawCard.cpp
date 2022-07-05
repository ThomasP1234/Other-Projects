#include "ElevensButtonEventHandlerDrawCard.h"
#include <iostream>

ElevensButtonEventHandlerDrawCard::ElevensButtonEventHandlerDrawCard(){}

ElevensButtonEventHandlerDrawCard::ElevensButtonEventHandlerDrawCard(Elevens *setElevens) {
    elevens = setElevens;
}

void ElevensButtonEventHandlerDrawCard::registerButtonManager(ElevensButtonManager *setbtnMgr) {
    btnMgr = setbtnMgr;
}

void ElevensButtonEventHandlerDrawCard::invoke(Button *btn) {    
    // btnMgr->remove(reinterpret_cast<ElevensButton*>(btn));
    // delete btn;

    Elevens *Game = Game->getInstance();
    Game->newButton();
}