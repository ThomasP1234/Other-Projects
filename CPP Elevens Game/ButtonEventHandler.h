#pragma once

#include "button.h"
#include "ButtonManager.h"

class ButtonEventHandler {
    public:
        ButtonEventHandler();
        virtual void invoke(class Button *btn) = 0;        
        //virtual void registerButtonManager(class ButtonManager *setbtnMgr) = 0;
        virtual ~ButtonEventHandler();
};
