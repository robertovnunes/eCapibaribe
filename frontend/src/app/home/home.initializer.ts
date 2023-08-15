import { APP_INITIALIZER } from '@angular/core';
import { HomeFacade } from './home.facade';

export const homeInitializer = (homeFacade: HomeFacade) => () => {
    homeFacade.fetchItems();
};

export const HomeInitializerProvider = {
    provide: APP_INITIALIZER,
    useFactory: homeInitializer,
    multi: true,
    deps: [HomeFacade],
};
