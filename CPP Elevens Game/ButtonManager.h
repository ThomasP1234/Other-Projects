#pragma once
#include <vector>
#include <algorithm>
#include "button.h"

class Button;

class ButtonManager {
protected:
    std::vector<Button*> buttons;
public:
    std::string type = "ButtonManager";
    virtual void add(Button *btn) = 0;
    virtual void remove(Button *btn) = 0;
    virtual void update() = 0;
    virtual void draw() = 0;
    virtual void destroy() = 0;
    virtual std::vector<Button*> get(){
        return buttons; 
    }
};
