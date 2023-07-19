import { CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { MatCardModule } from '@angular/material/card';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { MatListModule } from '@angular/material/list';

import { HomeRoutingModule } from './home-routing.module';
import { HomeComponent } from './pages/home/home.component';
import { SharedModule } from '../shared/shared.module';
import { CreateItemComponent } from './components/create-item/create-item.component';
import { ItemsComponent } from './pages/items/items.component';
import { ListItemsComponent } from './components/list-items/list-items.component';
import { HomeFacade } from './home.facade';
import { HomeApi } from './api/home.api';
import { HomeState } from './state/home.state';
import { HomeInitializerProvider } from './home.initializer';

@NgModule({
    declarations: [
        HomeComponent,
        CreateItemComponent,
        ItemsComponent,
        ListItemsComponent,
    ],
    imports: [
        CommonModule,
        HomeRoutingModule,
        SharedModule,
        MatCardModule,
        MatFormFieldModule,
        MatInputModule,
        MatListModule,
    ],
    providers: [HomeFacade, HomeApi, HomeState, HomeInitializerProvider],
    schemas: [CUSTOM_ELEMENTS_SCHEMA],
})
export class HomeModule {}
