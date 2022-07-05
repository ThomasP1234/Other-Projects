#pragma once

#include <string>
#include <vector>
#include "button.h"
#include "ButtonManager.h"

class ElevensButtonManager : public ButtonManager {
private:    
public:
    std::string type = "ElevensButtonManager";
    ElevensButtonManager();
    void add(Button *btn);
    void remove(Button *btn);
    void update();
    void draw();
    void destroy();    
};