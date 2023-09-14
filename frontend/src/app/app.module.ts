import { CreateCategoriesComponent } from './components/pages/categories/create-categories/create-categories.component';
import {FormsModule, ReactiveFormsModule} from "@angular/forms";
import { LoginComponent } from './components/pages/login/login.component';
import { HomeComponent } from './components/home/home.component';
import { CategoriesManagerComponent } from './components/pages/categories/categories-manager/categories-manager.component';
import { ListCategoriesComponent } from './components/pages/categories/list-categories/list-categories.component';
import { ButtonComponent } from './components/shared/layout/button/button.component';
import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';

import { AppComponent } from './app.component';
import { AppRoutingModule } from './app-routing.module';
import { ItemsModule } from './features/items/items.module';
import { UsersModule } from './features/users/users.module';
import { NavbarComponent } from './navbar/navbar.component';

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
      ReactiveFormsModule,
      HttpClientModule,
      BrowserModule,
      AppRoutingModule,
      FormsModule,
      ItemsModule,
      UsersModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
