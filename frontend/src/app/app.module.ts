import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { UserLoginComponent } from './components/user-login/user-login.component';
import { ItemCategoryComponent } from './components/item-category/item-category.component';
import { MainComponent } from './components/main/main.component';
import { ButtonComponent } from './components/view/button/button.component';

@NgModule({
  declarations: [
    AppComponent,
    UserLoginComponent,
    ItemCategoryComponent,
    MainComponent,
    ButtonComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
