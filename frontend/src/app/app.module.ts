
import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from "@angular/common/http";

import { NgIconsModule } from '@ng-icons/core';
import { heroUsers } from '@ng-icons/heroicons/outline';

import { AppComponent } from './app.component';
import {AppRoutingModule} from "./app-routing.module";

import { CreateCategoriesComponent } from './components/pages/categories/create-categories/create-categories.component';
import {FormsModule, ReactiveFormsModule} from "@angular/forms";
import { LoginComponent } from './components/pages/login/login.component';
import { HomeComponent } from './components/home/home.component';
import { CategoriesManagerComponent } from './components/pages/categories/categories-manager/categories-manager.component';
import { ListCategoriesComponent } from './components/pages/categories/list-categories/list-categories.component';
import { NavbarComponent } from './components/shared/layout/navbar/navbar.component';
import { ButtonComponent } from './components/shared/layout/button/button.component';

@NgModule({
  declarations: [
    AppComponent,
    CreateCategoriesComponent,
    LoginComponent,
    HomeComponent,
    CategoriesManagerComponent,
    ListCategoriesComponent,
    NavbarComponent,
    ButtonComponent

  ],
    imports: [
        BrowserModule,
        FormsModule,
        ReactiveFormsModule,
        AppRoutingModule,
        HttpClientModule,
        NgIconsModule.withIcons({ heroUsers }),
    ],
  providers: [],
  bootstrap: [AppComponent],
})
export class AppModule { }
