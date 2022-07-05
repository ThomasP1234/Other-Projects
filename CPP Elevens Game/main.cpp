#include "Elevens.h"

Elevens *Elevens::instance = 0;

int main(void) {   
    Elevens *Game = Game->getInstance();
    Game->gameLoop();    
    delete Game;
    return 0;
}