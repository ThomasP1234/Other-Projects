#pragma once

#include "button.h"
#include "ElevensButton.h"
#include "ButtonEventHandler.h"
#include "Elevens.h"
#include "ElevensButtonManager.h"
class Elevens;
class ElevensButtonEventHandler : public ButtonEventHandler {
    private:
        Elevens *elevens;
    public:
        ElevensButtonManager *btnMgr;

        ElevensButtonEventHandler();
        ElevensButtonEventHandler(Elevens* setElevens);

        void registerButtonManager(ElevensButtonManager *setbtnMgr);
        void invoke(Button *btn);
};